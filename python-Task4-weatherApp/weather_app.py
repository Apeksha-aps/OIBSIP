# Project: Basic Weather App (OIBSIP - Python Programming Task 4)
# Author: Apeksha Suhas Phapale

import requests

# Mapping WMO weather codes to readable descriptions
WEATHER_CONDITIONS = {
    0: "Clear Sky",
    1: "Mainly Clear",
    2: "Partly Cloudy",
    3: "Overcast",
    45: "Foggy",
    48: "Depositing Rime Fog",
    51: "Light Drizzle",
    53: "Moderate Drizzle",
    55: "Dense Drizzle",
    61: "Slight Rain",
    63: "Moderate Rain",
    65: "Heavy Rain",
    71: "Slight Snowfall",
    73: "Moderate Snowfall",
    75: "Heavy Snowfall",
    80: "Slight Rain Showers",
    81: "Moderate Rain Showers",
    82: "Violent Rain Showers",
    95: "Thunderstorm",
}

def get_coordinates(location_query):
    """Fetches latitude, longitude, and resolved name for a city or ZIP code."""
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": location_query, "count": 1, "language": "en", "format": "json"}
    response = requests.get(geo_url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    if "results" not in data or not data["results"]:
        return None

    place = data["results"][0]
    full_name = f"{place.get('name')}, {place.get('country', '')}".strip(", ")
    return place["latitude"], place["longitude"], full_name

def fetch_current_weather(lat, lon):
    """Fetches real-time weather metrics from Open-Meteo JSON API."""
    weather_url ="https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m",
        "wind_speed_unit": "kmh",
    }
    response = requests.get(weather_url, params=params, timeout=10)
    response.raise_for_status()
    return response.json().get("current", {})

def run_weather_app():
    print("\n" + "=" * 48)
    print("      PYTHON BASIC WEATHER APP - APEKSHA        ")
    print("=" * 48)

    while True:
        location = input("\nEnter city name or ZIP code (or 'exit' to quit): ").strip()

        if location.lower() in ("exit", "quit"):
            print("\nThank you for using Apeksha's Weather App. Goodbye!")
            break

        # Input validation: reject empty input
        if not location:
            print("Error: City name or ZIP code cannot be empty. Please try again.")
            continue

        try:
            coords = get_coordinates(location)
            if not coords:
                print(f"Error: Location '{location}' not found. Please check the spelling.")
                continue

            lat, lon, resolved_name = coords
            weather = fetch_current_weather(lat, lon)

            temp_c = weather.get("temperature_2m")
            temp_f = (temp_c * 9 / 5) + 32 if temp_c is not None else None
            humidity = weather.get("relative_humidity_2m")
            wind_speed = weather.get("wind_speed_10m")
            code = weather.get("weather_code")
            condition = WEATHER_CONDITIONS.get(code, "Moderate Weather")

            print("\n---------------- WEATHER REPORT ----------------")
            print(f"Location    : {resolved_name}")
            print(f"Temperature : {temp_c:.1f} °C  |  {temp_f:.1f} °F")
            print(f"Humidity    : {humidity}%")
            print(f"Condition   : {condition}")
            print(f"Wind Speed  : {wind_speed} km/h")
            print("------------------------------------------------")

        except requests.exceptions.Timeout:
            print("Network Error: Request timed out. Please check your internet connection.")
        except requests.exceptions.HTTPError as http_err:
            if http_err.response is not None and http_err.response.status_code == 401:
                print("API Error: Invalid or unauthorized API key.")
            else:
                print(f"API Error: Failed to retrieve data ({http_err}).")
        except requests.exceptions.RequestException:
            print("Network Error: Unable to connect to the weather service.")

if __name__ == "__main__":
    run_weather_app()
