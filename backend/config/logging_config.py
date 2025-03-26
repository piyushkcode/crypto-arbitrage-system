# backend/app/config/logging_config.py
import logging
import os
from logging.handlers import RotatingFileHandler

def configure_logging():
    """
    Configure comprehensive logging for the application
    """
    # Ensure logs directory exists
    log_dir = os.path.join(os.getcwd(), 'logs')
    os.makedirs(log_dir, exist_ok=True)

    # Configure root logger
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Create file handler
    file_handler = RotatingFileHandler(
        os.path.join(log_dir, 'crypto_arbitrage.log'),
        maxBytes=10 * 1024 * 1024,  # 10 MB
        backupCount=5
    )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    ))

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter(
        '%(name)s - %(levelname)s - %(message)s'
    ))

    # Get the root logger and add handlers
    root_logger = logging.getLogger()
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)

    # Set log levels for specific loggers
    logging.getLogger('ccxt').setLevel(logging.WARNING)
    logging.getLogger('urllib3').setLevel(logging.WARNING)
    logging.getLogger('websockets').setLevel(logging.WARNING)

    return root_logger

# Configure logging when this module is imported
root_logger = configure_logging()