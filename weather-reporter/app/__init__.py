from flask import Flask

# Create Flask application instance
app = Flask(__name__)

# Load configuration
app.config.from_object('app.config.Config')

# Import routes AFTER creating the app to avoid circular imports
from app.main import main  # This is your blueprint

# Register blueprint
app.register_blueprint(main)