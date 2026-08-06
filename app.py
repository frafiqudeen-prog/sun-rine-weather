from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

# Add your OpenWeatherMap API key here
API_KEY = "7d28a1b7602d1199f9e17b954378d448"

CURRENT_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/weather")
def get_weather():
    city = request.args.get("city", "").strip()

    if not city:
        return jsonify({"error": "Please enter a city name."}), 400

    if API_KEY == "YOUR_OPENWEATHERMAP_API_KEY":
        return jsonify({
            "error": "Please add your OpenWeatherMap API key in app.py."
        }), 500

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        current_response = requests.get(CURRENT_URL, params=params, timeout=10)
        forecast_response = requests.get(FORECAST_URL, params=params, timeout=10)

        if current_response.status_code != 200:
            return jsonify({"error": "City not found. Please check the city name."}), 404

        current = current_response.json()
        forecast = forecast_response.json()

        daily = {}
        for item in forecast.get("list", []):
            date = datetime.fromtimestamp(item["dt"]).strftime("%Y-%m-%d")

            if date not in daily:
                daily[date] = {
                    "date": date,
                    "temperature": item["main"]["temp"],
                    "min_temp": item["main"]["temp_min"],
                    "max_temp": item["main"]["temp_max"],
                    "description": item["weather"][0]["description"],
                    "icon": item["weather"][0]["icon"],
                    "humidity": item["main"]["humidity"],
                    "wind_speed": item["wind"]["speed"]
                }
            else:
                daily[date]["min_temp"] = min(
                    daily[date]["min_temp"], item["main"]["temp_min"]
                )
                daily[date]["max_temp"] = max(
                    daily[date]["max_temp"], item["main"]["temp_max"]
                )

        forecast_days = list(daily.values())[:5]

        return jsonify({
            "current": {
                "city": current["name"],
                "country": current["sys"]["country"],
                "temperature": current["main"]["temp"],
                "feels_like": current["main"]["feels_like"],
                "humidity": current["main"]["humidity"],
                "wind_speed": current["wind"]["speed"],
                "description": current["weather"][0]["description"],
                "icon": current["weather"][0]["icon"]
            },
            "forecast": forecast_days
        })

    except requests.exceptions.RequestException:
        return jsonify({
            "error": "Unable to connect to the weather service."
        }), 503


if __name__ == "__main__":
    app.run(debug=True)
