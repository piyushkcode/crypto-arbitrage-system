# backend/app/routes.py
from flask import jsonify, request
from .middleware.auth_middleware import authenticate_request
from .middleware.rate_limiter import rate_limit

def setup_routes(app, dependencies):
    exchanges = dependencies['exchanges']
    websocket_manager = dependencies['websocket_manager']
    trading_service = dependencies['trading_service']
    ml_predictor = dependencies['ml_predictor']

    @app.route('/api/arbitrage/detect', methods=['GET'])
    @authenticate_request
    @rate_limit()
    async def detect_arbitrage():
        symbol = request.args.get('symbol', 'BTC/USDT')
        arbitrage_service = trading_service.arbitrage_service
        opportunities = await arbitrage_service.detect_simple_arbitrage(symbol)
        return jsonify(opportunities)

    @app.route('/api/predict', methods=['POST'])
    @authenticate_request
    @rate_limit()
    def predict_arbitrage():
        data = request.json
        prediction = ml_predictor.predict_arbitrage(data)
        return jsonify({"predicted_spread": prediction})

    @app.route('/api/trade', methods=['POST'])
    @authenticate_request
    @rate_limit()
    async def execute_trade():
        opportunity = request.json
        result = await trading_service.execute_arbitrage_trade(opportunity)
        return jsonify({"success": result})

    @app.route('/api/exchanges', methods=['GET'])
    def get_exchanges():
        return jsonify([ex.name for ex in exchanges])

    # WebSocket routes
    @app.route('/ws/subscribe', methods=['POST'])
    async def subscribe_to_websocket():
        data = request.json
        await websocket_manager.connect(
            data['exchange'], 
            data['symbols'], 
            data.get('callback')
        )
        return jsonify({"status": "connected"})

    return app