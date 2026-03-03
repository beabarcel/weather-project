import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(lat, lon, api_key):
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()

    return response.json()
