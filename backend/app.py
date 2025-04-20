import os
from datetime import datetime
from functools import lru_cache

import feedparser
import openapi_client
import requests
import markdown

import chatbot
from flask import Flask, jsonify, request, session
from flask_cors import CORS
from flask_socketio import SocketIO
from openapi_client import ApiException

from lib import *

chatbots = {}
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/api/campus-events/today', methods=['GET'])
def today():
    try:
        return jsonify(fetch_campus_org_events(""))
    except ApiException as e:
        print("Exception when calling DefaultApi->astra_events: %s\n" % e)
    return jsonify({"error": True})


@app.route('/api/news', methods=['GET'])
def get_rss():
    max_entries = 20
    result = get_campus_news(max_entries)
    return jsonify(result)


@app.route('/api/campus-weather', methods=['GET'])
def get_weather():
    return jsonify(fetch_campus_weather()), 200



@app.route('/api/chat', methods=['POST'])
def chat_endpoint():
    """
    Handles chat requests using in-memory chatbot instances per user_id.
    """
    # 1. Get message and user_id from POST request body (JSON)
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    user_message = data.get('message')
    user_id = data.get('user_id') # Client MUST provide a persistent user_id

    if not user_message:
        return jsonify({"error": "Missing 'message' key in JSON payload"}), 400
    if not user_id:
        # Crucial: Need the client to identify itself consistently
        return jsonify({"error": "Missing 'user_id' key in JSON payload"}), 400

    # --- Accessing the global dictionary ---
    # Optional: Use lock if concerned about race conditions in a threaded environment
    # with chatbot_lock:
    # Find or create the chatbot instance for this user_id
    if user_id in chatbots:
        chatbot_instance = chatbots[user_id]
        print(f"--- Using existing Chatbot instance for user '{user_id}' ---")
    else:
        # Create a new instance if this user_id hasn't been seen before
        chatbot_instance = chatbot.Chatbot()
        chatbots[user_id] = chatbot_instance # Store the new instance

    # 3. Use the chatbot instance to get a response
    try:
        bot_response = chatbot_instance.ask(user_message)
    except Exception as e:
        print(f"Error during chatbot.ask() for user '{user_id}': {e}")
        # Consider removing the potentially broken instance?
        # with chatbot_lock:
        #     if user_id in chatbots: del chatbots[user_id]
        return jsonify({"error": "Internal server error during chat processing"}), 500

    # 4. No need to save state back - the object itself persists in the 'chatbots' dict

    # 5. Return the response
    return jsonify({"response": markdown.markdown(bot_response)})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
