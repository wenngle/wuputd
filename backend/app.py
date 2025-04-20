import os
from datetime import datetime
from functools import lru_cache

import feedparser
import openapi_client
import requests
from flask import Flask, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO
from openapi_client import ApiException

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

configuration = openapi_client.Configuration()
configuration.api_key['api_key'] = os.environ["API_KEY"]


def degrees_to_cardinal(degrees):
    """
    Convert wind direction in degrees to cardinal direction (N, NE, E, etc.)

    Args:
        degrees: Wind direction in degrees (0-360)

    Returns:
        String representing the cardinal direction
    """
    # Define direction ranges and their corresponding cardinal labels
    directions = [
        (348.75, 11.25, "N"),
        (11.25, 33.75, "NNE"),
        (33.75, 56.25, "NE"),
        (56.25, 78.75, "ENE"),
        (78.75, 101.25, "E"),
        (101.25, 123.75, "ESE"),
        (123.75, 146.25, "SE"),
        (146.25, 168.75, "SSE"),
        (168.75, 191.25, "S"),
        (191.25, 213.75, "SSW"),
        (213.75, 236.25, "SW"),
        (236.25, 258.75, "WSW"),
        (258.75, 281.25, "W"),
        (281.25, 303.75, "WNW"),
        (303.75, 326.25, "NW"),
        (326.25, 348.75, "NNW")
    ]

    # Handle None or invalid values
    if degrees is None:
        return None

    # Normalize degrees to 0-360 range
    degrees = float(degrees) % 360

    # Find the corresponding cardinal direction
    for min_deg, max_deg, direction in directions:
        if min_deg <= degrees < max_deg:
            return direction

    # Default to North for edge cases
    return "N"


def transform_nws_data(nws_data):
    """
    Transform NWS API observation data into simplified schema.

    Args:
        nws_data (dict): Raw NWS API observation data

    Returns:
        dict: Simplified weather data
    """
    # Extract properties from input data
    properties = nws_data.get("properties", {})

    # Extract and convert temperature (C to F)
    temp_c = properties.get("temperature", {}).get("value")
    temp_f = None
    if temp_c is not None:
        temp_f = round(temp_c * 9 / 5 + 32)

    # Extract wind speed (mph)
    wind_speed = int(int(properties.get("windSpeed", {}).get("value")) * 0.621371)

    wind_direction = degrees_to_cardinal(int(properties.get("windDirection", {}).get("value")))

    # Determine if it's day or night based on timestamp
    timestamp_str = properties.get("timestamp")
    is_daytime = True

    if timestamp_str:
        # Parse the timestamp
        timestamp = datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))

        # Simple day/night determination (6 AM to 6 PM is day)
        hour = timestamp.hour
        is_daytime = 6 <= hour < 18

    # Determine weather icon based on text description, cloud layers, and time of day
    text_description = properties.get("textDescription", "").lower()
    cloud_layers = properties.get("cloudLayers", [])

    # Determine icon based on conditions and time of day
    if is_daytime:
        # Day icons
        if "cloud" in text_description:
            if "mostly" in text_description or any(layer.get("amount") == "BKN" for layer in cloud_layers):
                icon = "⛅"  # Mostly cloudy
            elif "partly" in text_description or any(layer.get("amount") == "SCT" for layer in cloud_layers):
                icon = "🌤️"  # Partly cloudy
            else:
                icon = "☁️"  # Cloudy
        else:
            icon = "☀️"  # Clear/Sunny

        if "rain" in text_description or "shower" in text_description:
            icon = "🌧️"  # Rain
        elif "snow" in text_description:
            icon = "❄️"  # Snow
        elif "storm" in text_description or "thunder" in text_description:
            icon = "⛈️"  # Storm
        elif "fog" in text_description or "mist" in text_description:
            icon = "🌫️"  # Fog
    else:
        # Night icons
        if "cloud" in text_description:
            if "mostly" in text_description or any(layer.get("amount") == "BKN" for layer in cloud_layers):
                icon = "☁️"  # Cloudy night
            elif "partly" in text_description or any(layer.get("amount") == "SCT" for layer in cloud_layers):
                icon = "🌙"  # Partly cloudy night
            else:
                icon = "☁️"  # Cloudy
        else:
            icon = "🌙"  # Clear night

        if "rain" in text_description or "shower" in text_description:
            icon = "🌧️"  # Rain (same for day and night)
        elif "snow" in text_description:
            icon = "❄️"  # Snow (same for day and night)
        elif "storm" in text_description or "thunder" in text_description:
            icon = "⛈️"  # Storm (same for day and night)
        elif "fog" in text_description or "mist" in text_description:
            icon = "🌫️"  # Fog (same for day and night)

    # Estimate rain percentage based on cloud cover and humidity
    rain_percent = 0
    relative_humidity = properties.get("relativeHumidity", {}).get("value", 0)

    if relative_humidity is not None:
        # Simple estimation: higher humidity and more cloud cover = higher chance of rain
        cloud_coverage = 0
        for layer in cloud_layers:
            amount = layer.get("amount", "")
            if amount == "OVC":  # Overcast
                cloud_coverage += 0.8
            elif amount == "BKN":  # Broken
                cloud_coverage += 0.6
            elif amount == "SCT":  # Scattered
                cloud_coverage += 0.3
            elif amount == "FEW":  # Few
                cloud_coverage += 0.1

        # Cap cloud coverage at 1.0
        cloud_coverage = min(cloud_coverage, 1.0)

        # Calculate rain percentage based on humidity and cloud coverage
        rain_percent = round(cloud_coverage * (relative_humidity / 100) * 70)

        # If the description explicitly mentions rain or precipitation
        if any(term in text_description for term in ["rain", "shower", "drizzle", "precipitation"]):
            rain_percent = max(rain_percent, 70)  # At least 70% if rain is mentioned

    # Create the simplified schema
    simplified_data = {
        "icon": icon,
        "temp": temp_f,
        "wind_speed": wind_speed,
        "wind_direction": wind_direction,
        "rain_percent": rain_percent
    }

    return simplified_data


@lru_cache(maxsize=32)
def fetch_weather():
    # Example usage
    res = requests.get("https://api.weather.gov/stations/KADS/observations/latest")
    res.raise_for_status()
    return transform_nws_data(res.json())


# Cache parsed feeds to improve performance
@lru_cache(maxsize=32)
def fetch_and_parse_feed(max_entries=None):
    feeds = [
        ('UTD News', 'https://news.utdallas.edu/feed/'),
        ('AMP', 'https://www.ampatutd.com/feed/'),
        ('Retrograde', 'https://retrogradenews.com/feed/'),
        ('Voyager', 'https://engineering-magazine.utdallas.edu/feed/'),
    ]
    firehose = []
    for name, url in feeds:
        try:
            feed = feedparser.parse(url)
            i = 0
            for entry in feed.entries:
                if i < 11:
                    firehose.append({
                        'title': entry.title,
                        'link': entry.link,
                        'published': entry.published_parsed,
                        'updated': entry.updated_parsed,
                        'source': name,
                    })
                i += 1
        except Exception as e:
            pass
    return sorted(firehose, key=lambda entry: entry['updated'], reverse=True)[:max_entries]


@lru_cache(maxsize=32)
def get_org_events(date=datetime.now().date()):
    with openapi_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = openapi_client.DefaultApi(api_client)
        var_date = date.isoformat()  # str | date (ISO format) to retrieve astra events
        org_events = []
        api_response = api_instance.astra_events(var_date)
        for building in api_response.data.buildings:
            for room in building.rooms:
                for event in room.events:
                    if event.meeting_type in ("Student Organization", "ECSW Events"):
                        if event.activity_name not in [e['title'] for e in org_events]:
                            org_events.append({
                                'title': event.activity_name,
                                'start_date': event.start_date,
                                'end_date': event.end_date,
                                'location': f'{building.building} {room.room}',
                            })
        return org_events


@app.route('/api/campus-events/today', methods=['GET'])
def today():
    try:
        return jsonify(get_org_events())
    except ApiException as e:
        print("Exception when calling DefaultApi->astra_events: %s\n" % e)
    return jsonify({"error": True})


@app.route('/api/news', methods=['GET'])
def get_rss():
    max_entries = 20
    result = fetch_and_parse_feed(max_entries)
    return jsonify(result)


@app.route('/api/campus-weather', methods=['GET'])
def get_weather():
    return jsonify(fetch_weather()), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
