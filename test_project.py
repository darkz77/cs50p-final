import pytest
from project import get_location
from unittest.mock import patch


def test_get_location():
    ## assert 2 float latitde longitude for "Berlin"
    latitude, longitude = get_location("Berlin")
    assert latitude == pytest.approx(52.52437)
    assert longitude == pytest.approx(13.41053)


@patch("project.fetch_forecast_api")
def test_get_min_max_success(mock_fetch):
    mock_fetch.return_value


def fetch_forecast_api():
    pass