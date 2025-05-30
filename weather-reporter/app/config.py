import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class Config:
    OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
    SECRET_TOKEN = os.getenv("SECRET_TOKEN")
    RPC_PORT = int(os.getenv("RPC_PORT", 8001))
    WEB_PORT = int(os.getenv("WEB_PORT", 5000))
    BASE_URL = "https://api.openweathermap.org/data/2.5"
    NGROK_AUTH_TOKEN = os.getenv("NGROK_AUTH_TOKEN", "")

# Optionally, print the environment variables for debugging
print("OpenWeather API Key:", os.getenv("OPENWEATHER_API_KEY"))
print("Secret Token:", os.getenv("SECRET_TOKEN"))
