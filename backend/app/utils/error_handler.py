# backend/app/utils/error_handler.py
import logging
from functools import wraps

def handle_api_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"API Error in {func.__name__}: {e}")
            # You could add more sophisticated error handling here
            raise
    return wrapper