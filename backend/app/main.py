# backend/app/main.py
from flask import Flask
from flask_cors import CORS
from .routes import setup_routes
from .services.exchange_service import ExchangeService
from .services.machine_learning_service import MLArbitragePredictor
from .services.trading_service import TradingService
from .utils.websocket_handler import WebSocketManager
import logging

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Configure logging
    logging.basicConfig(level=logging.INFO)

    # Setup exchanges
    exchanges = [
        ExchangeService('binance'),
        ExchangeService('kraken'),
        ExchangeService('kucoin')
    ]

    # Initialize WebSocket Manager
    websocket_manager = WebSocketManager([ex.name for ex in exchanges])

    # Initialize ML Predictor (assuming you have historical data)
    historical_data = []  # Load from database or file
    ml_predictor = MLArbitragePredictor(historical_data)
    ml_predictor.train_model()

    # Initialize Trading Service
    trading_service = TradingService(exchanges, ml_predictor)

    # Setup routes and inject dependencies
    setup_routes(app, {
        'exchanges': exchanges,
        'websocket_manager': websocket_manager,
        'trading_service': trading_service,
        'ml_predictor': ml_predictor
    })

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)