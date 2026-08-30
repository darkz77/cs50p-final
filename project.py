import requests
import sys


def main():
    city_name = input("City name: ").strip()
    print(get_location(city_name))


def get_location(city_name: str):
    params = {
        "name": city_name,
        "count": 1,
        "language": "en",
        "format": "json"
    }
    response = requests.get("https://geocoding-api.open-meteo.com/v1/search", params=params)
    response.raise_for_status()
    data = response.json()
    results = data["results"]

    if results:
        latitude = results[0]["latitude"]
        longitude = results[0]["longitude"]
        return latitude, longitude

    print("City not found")
    sys.exit(1)


def get_min_max(latitude: float, longitude: float):
    ...


def get_forecast(latitude: float, longitude: float, forecast_days: int):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m",
        "forecast_days": forecast_days
    }
    response = requests.get("https://api.open-meteo.com/v1/forecast", params=params)
    response.raise_for_status()
    data = response.json()
    results = 



def get_current_temp():
    ...


def generate_table():
    ...


if __name__ == "__main__":
    main()