import pytest
from project import get_location, get_min_max, get_current_temp, get_forecast
from unittest.mock import patch


def test_get_location():
    ## assert 2 float latitde longitude for "Berlin"
    latitude, longitude = get_location("Berlin")
    assert latitude == pytest.approx(52.52437)
    assert longitude == pytest.approx(13.41053)


@patch("project.fetch_forecast_api")
def test_get_min_max(mock_data):
    mock_data.return_value = {
        "daily": {
            "time": ["2026-01-01", "2026-01-02"],
            "temperature_2m_min": [21.0, 22.5],
            "temperature_2m_max": [25.0, 28.0]
        }
    }

    latitude = 52.52
    longitude = 13.41

    result, headers = get_min_max(latitude, longitude)

    mock_data.assert_called_once_with(
        {
            "latitude": latitude,
            "longitude": longitude,
            "daily": ["temperature_2m_max", "temperature_2m_min"]
        }
    )

    assert headers == ["Time", "Min temperature 2m", "Max temperature 2m"]
    assert result == [
        ("2026-01-01", 21.0, 25.0),
        ("2026-01-02", 22.5, 28.0)
    ]


@patch("project.fetch_forecast_api")
def test_get_current_temp(mock_data):
    mock_data.return_value = {
        "current": {
            "temperature_2m": 27
        }
    }

    latitude = 52.52
    longitude = 13.41

    current_temp = get_current_temp(latitude, longitude)

    mock_data.assert_called_once_with(
        {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m"
        }
    )

    assert current_temp == 27


@patch("project.fetch_forecast_api")
@patch("builtins.input")
def test_get_forecast(mock_input, mock_data):
    mock_data.return_value = {
            "hourly": 
            {
                "time": [
                "2026-09-10T00:00",
                "2026-09-10T01:00"
                ],
                "temperature_2m": [15.6, 15]
            }   
    }

    mock_input.side_effect = ["1"]

    latitude = 52.52
    longitude = 13.419998
    forecast_days = 1

    result, headers = get_forecast(latitude, longitude)

    mock_input.assert_called_once_with("Number of days: ")

    mock_data.assert_called_once_with({
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m",
        "forecast_days": forecast_days
    })

    assert headers == ["Time", "Temperature"]
    assert result == [
        ("2026-09-10T00:00", 15.6), 
        ("2026-09-10T01:00", 15)
    ]
    