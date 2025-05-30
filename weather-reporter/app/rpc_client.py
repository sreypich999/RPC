from xmlrpc.client import ServerProxy
from app.config import Config
from app.utils.logging_config import setup_logger

config = Config()
logger = setup_logger(__name__)

class RPCClient:
    def __init__(self):
        self.server = ServerProxy(f"http://localhost:{config.RPC_PORT}")
        logger.info("RPC CLIENT: Connected to server")
        print("RPC Client initialized")

    def get_weather(self, city):
        try:
            logger.info(f"RPC CLIENT: Requesting weather for {city}")
            print(f"Requesting weather: {city}")
            result = self.server.get_weather(config.SECRET_TOKEN, city)
            logger.info(f"RPC CLIENT: Received weather for {city}")
            print(f"Weather data received for: {city}")
            return result
        except Exception as e:
            logger.error(f"RPC CLIENT: Weather error for {city}: {e}")
            raise

    def get_forecast(self, city):
        try:
            logger.info(f"RPC CLIENT: Requesting forecast for {city}")
            print(f"Requesting forecast: {city}")
            result = self.server.get_forecast(config.SECRET_TOKEN, city)
            logger.info(f"RPC CLIENT: Received forecast for {city}")
            print(f"Forecast data received for: {city}")
            return result
        except Exception as e:
            logger.error(f"RPC CLIENT: Forecast error for {city}: {e}")
            raise

if __name__ == "__main__":
    print("\n=== Testing RPC Client ===")
    client = RPCClient()
    try:
        print(client.get_weather("Phnom Penh"))
    except Exception as e:
        print(f"Test error: {e}")
    