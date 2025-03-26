# backend/app/middleware/__init__.py
# Initialize the middleware package
from .auth_middleware import authenticate_request
from .rate_limiter import rate_limit