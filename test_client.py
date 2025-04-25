# test_client.py
from dotenv import load_dotenv
load_dotenv()

from src.weatherlib.client import API_KEY

print("API_KEY from client.py:", repr(API_KEY))
