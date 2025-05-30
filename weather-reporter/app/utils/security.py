from app.config import Config
from app.utils.logging_config import setup_logger

config = Config()
logger = setup_logger(__name__)

def validate_token(token):
    """Validate authentication token with security logging"""
    try:
        is_valid = token == config.SECRET_TOKEN
        
        if is_valid:
            logger.info("Valid token accepted")
        else:
            logger.warning(
                f"Invalid token attempt: {token[:6]}... (length: {len(token)})"
            )
            
        return is_valid
    except Exception as e:
        logger.error(f"Token validation failed: {str(e)}")
        raise