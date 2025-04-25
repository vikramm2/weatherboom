# WeatherLib

**WeatherLib** is a lightweight Python library for fetching weather information via the free WeatherAPI.com service. It offers three simple, intuitive functions:

- **`get_location_temp(location: str) -> str`**
  - Returns the current temperature in Celsius for the given location (e.g., "Paris").
- **`get_todays_forecast(location: str) -> str`**
  - Provides today’s forecast summary including weather condition, high and low temperatures.
- **`is_sunny_day(date_str: str) -> str`**
  - Checks if a specified date (ISO format `YYYY-MM-DD`) within the next 3 days is forecasted as sunny, returning "Yes", "No", or an error message.


Video Demo:
https://drive.google.com/file/d/15jakm3bb4QPgRy6lPB_hkknYws3TeN51/view?usp=drive_link

## Project Structure

```plaintext
weatherboom/
├── .env.example               # Sample environment variables fileciteturn4view0
├── setup.py                   # Packaging configuration (defines `weatherlib` package)citeturn2view0
├── src/
│   └── weatherlib/
│       ├── client.py          # Loads API key and makes HTTP requests
│       └── weather.py         # Implements the three core functions
├── tests/
│   └── test_weatherlib.py     # Pytest suite covering all functions
├── run_weather_test.py        # Standalone executable script to demo usage
└── dist/                      # Built distributions (wheel & sdist)
    ├── weatherlib-0.1.0-py3-none-any.whl
    └── weatherlib-0.1.0.tar.gz
```citeturn0view0

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/vikramm2/weatherboom.git
   cd weatherboom
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install the package**
   ```bash
   pip install -e .
   ```

4. **Configure your API key**
   ```bash
   cp .env.example .env
   # Edit .env and set:
   WEATHERAPI_KEY=your_actual_key_here
   # (Optional) DEFAULT_LOCATION=auto:ip
   ```

## Usage

Use the library in your Python code:

```python
from weatherlib.weather import (
    get_location_temp,
    get_todays_forecast,
    is_sunny_day
)

print(get_location_temp("Paris"))             # e.g., "18.2°C"
print(get_todays_forecast("London"))         # e.g., "Sunny, High: 20°C, Low: 10°C"
print(is_sunny_day("2025-04-26"))           # e.g., "Yes" or "No"
```

Or run the demo script:

```bash
./run_weather_test.py
```

## Testing

Install test dependencies and run pytest:

```bash
pip install pytest
pytest -q
```

