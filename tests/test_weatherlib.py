# tests/test_weatherlib.py

import re
import pytest
from src.weatherlib.client import API_KEY
from src.weatherlib.weather import (
    get_location_temp,
    get_todays_forecast,
    is_sunny_day
)

@pytest.fixture(autouse=True)
def check_api_key():
    assert API_KEY, "WEATHERAPI_KEY must be set in .env"

def test_get_location_temp_format():
    temp = get_location_temp("New York")
    # Expect something like "12.3°C" or "-5.0°C"
    assert re.match(r"^-?\d+(\.\d+)?°C$", temp)

def test_get_todays_forecast_format():
    forecast = get_todays_forecast("London")
    # Expect "Condition, High: X°C, Low: Y°C"
    assert "High:" in forecast and "Low:" in forecast

def test_is_sunny_day_valid():
    # Use today’s date or a known date in the next 3 days
    from datetime import date
    today = date.today().isoformat()
    result = is_sunny_day(today)
    assert result in ("Yes", "No")

def test_is_sunny_day_invalid_date():
    result = is_sunny_day("not-a-date")
    assert result.startswith("Invalid date format")
