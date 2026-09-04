from project import get_location
import pytest

def test_get_location():
    ## assert 2 float latitde longitude for "Berlin"
    latitude, longitude = get_location("Berlin")
    assert latitude == pytest.approx(52.52437)
    assert longitude == pytest.approx(13.41053)


def test_get_min_max():
    pass


def fetch_forecast_api():
    pass