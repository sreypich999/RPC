from flask import Blueprint, render_template, request, jsonify
from app.services import WeatherService
from app.utils.logging_config import setup_logger

# Create blueprint instead of using app directly
main = Blueprint('main', __name__)
logger = setup_logger(__name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/api/weather', methods=['POST'])
def get_weather():
    try:
        city = request.json['city']
        logger.info(f"WEB: Received request for {city}")
        
        weather_service = WeatherService()
        data = weather_service.get_combined_weather(city)
        
        return jsonify(data)
    except Exception as e:
        logger.error(f"WEB Error: {str(e)}")
        return jsonify({'error': str(e)}), 500