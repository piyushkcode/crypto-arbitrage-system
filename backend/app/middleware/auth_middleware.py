# backend/app/middleware/auth_middleware.py
from functools import wraps
from flask import request, jsonify
import jwt
import os

def authenticate_request(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"error": "Authorization token is missing"}), 401
        
        try:
            # Verify the JWT token
            secret_key = os.environ.get('JWT_SECRET_KEY', 'your-secret-key')
            payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token has expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401
        
        return f(*args, **kwargs)
    return decorated_function