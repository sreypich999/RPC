from app.rpc_client import RPCClient
from datetime import datetime
from app.utils.logging_config import setup_logger

logger = setup_logger(__name__)

class WeatherService:
    def __init__(self):
        self.rpc = RPCClient()
        logger.info("SERVICE: RPC client initialized")

    def get_combined_weather(self, city):
        try:
            logger.info(f"SERVICE: Getting weather for {city}")
            current = self.rpc.get_weather(city)
            forecast = self.rpc.get_forecast(city)
            
            logger.debug(f"SERVICE: Processed {city} data")
            return {
                'current': self.process_current(current),
                'forecast': self.process_forecast(forecast.get('list', []))
            }
        except Exception as e:
            logger.error(f"SERVICE: Error for {city}: {str(e)}")
            raise

    def process_current(self, data):
        return {
            'temp': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'humidity': data['main']['humidity'],
            'wind': data['wind']['speed'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
            'timestamp': datetime.now().isoformat()
        }

    def process_forecast(self, forecast_list):
        return [{
            'dt': item['dt'],
            'temp': item['main']['temp'],
            'humidity': item['main']['humidity'],
            'wind': item['wind']['speed'],
            'description': item['weather'][0]['description'],
            'icon': item['weather'][0]['icon']
        } for item in forecast_list]