import os

from flask import Flask, jsonify
from flask_cors import CORS
import openapi_client
from openapi_client import ApiException

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

configuration = openapi_client.Configuration()
configuration.api_key['api_key'] = os.environ["API_KEY"]

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello from Flask!"})

@app.route('/api/campus-events/today', methods=['GET'])
def today():
    with openapi_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = openapi_client.DefaultApi(api_client)
        var_date = 'var_date_example'  # str | date (ISO format) to retrieve astra events

        try:
            api_response = api_instance.astra_events(var_date)
            print("The response of DefaultApi->astra_events:\n")
            return jsonify(api_response)
        except ApiException as e:
            print("Exception when calling DefaultApi->astra_events: %s\n" % e)
    return jsonify({ "error": True })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)