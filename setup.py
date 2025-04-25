from setuptools import setup, find_packages

setup(
    name="weatherlib",
    version="0.1.0",
    author="Vikram M",
    author_email="vikram2@umbc.edu",
    description="A Python library to fetch weather information using WeatherAPI.com",
    long_description="weatherboom is a lightweight Python library for fetching weather information using the free WeatherAPI.com service. It provides three simple functions: get_location_temp(location: str) -> str: Returns the current temperature in Celsius for the specified location. get_todays_forecast(location: str) -> str: Returns today's forecast summary (condition, high, low) for the specified location. is_sunny_day(date_str: str) -> str: Returns Yes if the target date is forecasted as sunny (within the next 3 days), No otherwise, or an error message for invalid dates.",
    url="https://github.com/vikramm2/weatherboom",
    license="MIT",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "requests>=2.20.0",
        "python-dotenv>=0.19.0",
    ],
    python_requires=">=3.7",
)
