import sys
import requests
from tabulate import tabulate

url_forecast = "https://api.open-meteo.com/v1/forecast"

def main() -> None:
    while True:
        try:
            input_option = input("(M)in Max Daily - (F)orecast - (C)urrent Temperature - (Q)uit - (R)estart: ").strip().lower()
            city_name = input("City name: ").strip()
            latitude, longitude = get_location(city_name)

            if input_option == "m":
                result, headers = get_min_max(latitude, longitude)
                generate_table(result, headers)

            if input_option == "f":
                result, headers = get_forecast()
                generate_table(result, headers)

            if input_option == "c":
                print(f"The current temperature is {get_current_temp(latitude, longitude)} Celcius!")

            if input_option == "r":
                main()

            if input_option == "q":
                print("Shutdown...")
                sys.exit(0)

        except ValueError:
            continue
    

def get_location(city_name: str):
    """
    This function will search the city using Open Meteo's Search API

    :param city_name: Name of city you want to search
    :type city_name: str
    :return: Description
    :rtype: Any
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
    """
    Docstring for get_min_max
    
    :param latitude: Location's latitude
    :type latitude: float
    :param longitude: Location's longitude
    :type longitude: float
    :return: Description
    :rtype: Any
    """
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": ["temperature_2m_max", "temperature_2m_min"]
    }
    response = requests.get(url_forecast, params=params)
    response.raise_for_status()
    data = response.json()

    if data["daily"]:
        time = data["daily"]["time"]
        min = data["daily"]["apparent_temperature_min"]
        max = data["daily"]["apparent_temperature_max"]
        result = list(zip(time, min, max))
        headers = ["Time", "Min apparent temperature", "Max apparent temperature"]
        return result, headers


def get_forecast(latitude: float, longitude: float) -> dict:
    """
    This function return a table of forecast for 2m height from Open Meteo's forecast API

    :param latitude: Location's latitude
    :type latitude: float
    :param longitude: Location's longitude
    :type longitude: float
    :param forecast_days: Description
    :type forecast_days: int
    :return: number of days to return the weather forecast. Default 7 days, maximum 16 days
    :rtype: dict
    """
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m",
        "forecast_days": forecast_days
    }
    while True:
        try:
            forecast_days = int(input("Number of days: ").strip())
            break

        except ValueError:
            print("Invalid number!")
            continue

    response = requests.get(url_forecast, params=params)
    response.raise_for_status()
    data = response.json()

    if data["error"]:
        print(data["reason"])
    if data["hourly"]:
        time = data["hourly"]["time"]
        temperature = data["hourly"]["temperature_2m"]
        result = list(zip(time, temperature))
        headers = ["Time", "Temperature"]
        return result, headers


def get_current_temp(latitude: float, longitude: float) -> str:
    """
    Docstring for get_current_temp
    
    :param latitude: Location's latitude
    :type latitude: float
    :param longitude: Location's longitude
    :type longitude: float
    :return: a str of current temperature
    :rtype: str
    """
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m",
    }
    response = requests.get(url_forecast, params=params)
    response.raise_for_status()
    data = response.json()

    if data["current"]:
        return data["current"]["temperature_2m"]


def generate_table(result, headers):
    """
    Docstring for generate_table

    :param result: Description
    :param headers: Description
    :return: Description
    :rtype: str
    """
    return tabulate(result, headers=headers, tablefmt="grid")


if __name__ == "__main__":
    main()
