from .client import get_current_weather, get_forecast
from datetime import datetime

def get_location_temp(location: str) -> str:
    data = get_current_weather(location)
    temp_c = data["current"]["temp_c"]
    return f"{temp_c}°C"

def get_todays_forecast(location: str) -> str:
    data = get_forecast(location, days=1)
    day = data["forecast"]["forecastday"][0]["day"]
    return (f"{day['condition']['text']}, "
            f"High: {day['maxtemp_c']}°C, "
            f"Low: {day['mintemp_c']}°C")

def is_sunny_day(date_str: str) -> str:
    try:
        target = datetime.fromisoformat(date_str).date()
    except ValueError:
        return f"Invalid date format: {date_str}"

    data = get_forecast("auto:ip", days=3)
    for day in data["forecast"]["forecastday"]:
        if day["date"] == target.isoformat():
            cond = day["day"]["condition"]["text"]
            return "Yes" if "Sunny" in cond else "No"
    return f"No forecast available for {date_str}"
