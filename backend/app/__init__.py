# backend/app/__init__.py
from flask import Flask
from flask_cors import CORS
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def create_app():
    """
    Application factory function to create and configure the Flask application
    """
    app = Flask(__name__)
    
    # Configure CORS
    CORS(app, resources={
        r"/api/*": {
            "origins": "*",
            "allow_headers": [
                "Content-Type", 
                "Authorization", 
                "Access-Control-Allow-Credentials"
            ],
            "supports_credentials": True
        }
    })

    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler('crypto_arbitrage.log')
        ]
    )

    # Import and register blueprints/routes here if using blueprints
    # from .routes import main_blueprint
    # app.register_blueprint(main_blueprint)

    # Configure application settings
    app.config.update(
        SECRET_KEY='your-secret-key',  # Replace with a strong secret key
        DEBUG=True,  # Set to False in production
        ARBITRAGE_THRESHOLD=1.5,  # Minimum profit percentage
        MAX_TRADE_AMOUNT=1000,  # Maximum trade amount in USD
    )

    return app