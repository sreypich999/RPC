from xmlrpc.server import SimpleXMLRPCServer
from socketserver import ThreadingMixIn
from concurrent.futures import ThreadPoolExecutor
from app.config import Config
import requests
import logging

config = Config()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class ThreadedXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    allow_reuse_address = True
    daemon_threads = True

def authenticate(func):
    def wrapper(self, token, *args, **kwargs):
        if token != config.SECRET_TOKEN:
            logger.warning("AUTH: Invalid token attempt")
            raise ValueError("Invalid token")
        return func(self, token, *args, **kwargs)
    return wrapper

class WeatherService:
    def __init__(self):
        self.executor = ThreadPoolExecutor(max_workers=10)
        logger.info("RPC SERVER: Service initialized")

    @authenticate
    def get_weather(self, token, city):
        logger.info(f"RPC SERVER: Weather request for {city}")
        print(f"Processing weather for: {city}")
        return self._fetch_data(city, 'weather')

    @authenticate
    def get_forecast(self, token, city):
        logger.info(f"RPC SERVER: Forecast request for {city}") 
        print(f"Processing forecast for: {city}")
        return self._fetch_data(city, 'forecast')

    def _fetch_data(self, city, endpoint):
        try:
            logger.debug(f"RPC SERVER: Fetching {endpoint} for {city}")
            response = requests.get(
                f"{config.BASE_URL}/{endpoint}",
                params={
                    'q': city,
                    'appid': config.OPENWEATHER_API_KEY,
                    'units': 'metric'
                }
            )
            response.raise_for_status()
            logger.info(f"RPC SERVER: Successfully fetched {endpoint} for {city}")
            return response.json()
        except Exception as e:
            logger.error(f"RPC SERVER: Error for {city}: {str(e)}")
            raise

def run_server():
    server = ThreadedXMLRPCServer(("0.0.0.0", config.RPC_PORT), allow_none=True)
    server.register_instance(WeatherService())
    logger.info(f"RPC SERVER: Running on port {config.RPC_PORT}")
    print("=== RPC Server Started ===")
    server.serve_forever()

if __name__ == "__main__":
    run_server()