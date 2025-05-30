from functools import wraps
from app.config import Config
from app.utils.logging_config import setup_logger

config = Config()
logger = setup_logger(__name__)

def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = args[1]
        if token != config.SECRET_TOKEN:
            logger.warning("Invalid authentication attempt")
            raise PermissionError("Invalid authentication token")
        return func(*args, **kwargs)
    return wrapper