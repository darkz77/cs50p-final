import requests
import sys
from tabulate import tabulate


def main():
    city_name = input("City name: ").strip()
    latitude, longitude = get_location(city_name)
    print(latitude, longitude)

    forecast_table = get_current_temp(latitude, longitude)
    print(f"Current temperature is {forecast_table}°C")
    


def get_location(city_name: str) -> ():
    """
    This function will search the city using Open Meteo's Search API
    Then return the latitude and longitude of the 1st city found
        input - city name: str
        return - tuple with 2 values of latitude and logitude
    """
    params = {
        "name": city_name,
        "count": 1,
        "language": "en",
        "format": "json"
    }
    response = requests.get("https://geocoding-api.open-meteo.com/v1/search", params=params)
    response.raise_for_status()
    try :
        data = response.json()
        results = data["results"]
    except KeyError:
        print("City not found")
        sys.exit(1)

    if results:
        latitude = results[0]["latitude"]
        longitude = results[0]["longitude"]
        return latitude, longitude


def get_min_max(latitude: float, longitude: float):
    ...


def get_forecast(latitude: float, longitude: float, forecast_days: int) -> dict:
    """
    This function return a table of forecast for 2m height from Open Meteo's forecast API
        Input:
        latitude: float - The location's latitude
        longitude: float - The location's longitude
        forecast_days: int - number of days to return the weather forecast. Default 7 days, maximum 16 days
    """
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m",
        "forecast_days": forecast_days
    }
    response = requests.get("https://api.open-meteo.com/v1/forecast", params=params)
    response.raise_for_status()
    data = response.json()

    if data["error"]:
        print(data["reason"])
    if data["hourly"]:
        return data["hourly"]
    return None


def get_current_temp(latitude: float, longitude: float) -> str:
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m",
    }
    response = requests.get("https://api.open-meteo.com/v1/forecast", params=params)
    response.raise_for_status()
    data = response.json()

    if data["current"]:
        return data["current"]["temperature_2m"]


def generate_table(dict: dict):
    """
    This function format the returned forecast data to a readable table format using Tabulate
        input: dict - A dict json returned from Open Meteo's API
        return: A formatted table using Tabulate
    """
    time = dict["time"]
    temperature = dict["temperature_2m"]
    result = list(zip(time, temperature))
    headers = ["Time", "Temperature in C"]
    return tabulate(result, headers=headers, floatfmt="grid")


if __name__ == "__main__":
    main()
