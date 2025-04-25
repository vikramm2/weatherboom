#!/usr/bin/env python3
import sys
import os

# Insert the 'src' directory (where weatherlib lives) onto sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from weatherlib.client import get_current_weather, get_forecast
from weatherlib.weather import get_location_temp, get_todays_forecast, is_sunny_day
from datetime import datetime


def main():
    location = "Memphis"
    print(f"get_location_temp('{location}'): {get_location_temp(location)}")

    print(f"get_todays_forecast('{location}'): {get_todays_forecast(location)}")

    # Test is_sunny_day for today
    today = datetime.today().date().isoformat()
    print(f"is_sunny_day('{today}'): {is_sunny_day(today)}")

    # Example test for a specific date (ISO format)
    test_date = (datetime.today().date()).isoformat()
    print(f"is_sunny_day('{test_date}'): {is_sunny_day(test_date)}")


if __name__ == "__main__":
    main()

