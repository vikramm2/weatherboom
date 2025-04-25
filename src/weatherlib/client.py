import os
import requests
from pathlib import Path
from dotenv import load_dotenv





# Step 1: build the path to your .env file in the project root
# (__file__ is .../src/weatherlib/client.py, so parents[2] is the project root)
env_path = Path(__file__).resolve().parents[2] / ".env"

# Step 2: load explicitly from that path
load_dotenv(dotenv_path=env_path)

# Now retrieve the key
API_KEY = os.getenv("WEATHERAPI_KEY")
if not API_KEY:
    raise RuntimeError(f"WEATHERAPI_KEY not found at {env_path}")


BASE_URL = "https://api.weatherapi.com/v1"

def _make_request(endpoint: str, params: dict) -> dict:
    """
    Internal: hit the given endpoint (e.g. 'current', 'forecast') 
    and return the parsed JSON.
    """
    url = f"{BASE_URL}/{endpoint}.json"
    params.update({"key": API_KEY})
    resp = requests.get(url, params=params, timeout=5)
    resp.raise_for_status()
    return resp.json()

def get_current_weather(location: str) -> dict:
    """
    Returns the full JSON payload for current weather at `location`.
    """
    return _make_request("current", {"q": location})

def get_forecast(location: str, days: int = 1) -> dict:
    """
    Returns the full JSON payload for forecast for `days` ahead.
    """
    return _make_request("forecast", {"q": location, "days": days})



