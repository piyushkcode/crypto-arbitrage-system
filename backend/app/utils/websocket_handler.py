# backend/app/utils/websocket_handler.py
import websockets
import asyncio
import json
from typing import Callable, List

class WebSocketManager:
    def __init__(self, exchanges: List[str]):
        self.exchanges = exchanges
        self.connections = {}

    async def connect(self, exchange: str, symbols: List[str], callback: Callable):
        """
        Connect to WebSocket for specific exchange and symbols
        """
        try:
            # This is a generic implementation. Each exchange has different WebSocket APIs
            if exchange == 'binance':
                uri = f"wss://stream.binance.com:9443/ws/{'/'.join(symbols)}"
            elif exchange == 'coinbase':
                uri = "wss://ws-feed.pro.coinbase.com"
            else:
                raise ValueError(f"Unsupported exchange: {exchange}")

            async with websockets.connect(uri) as websocket:
                self.connections[exchange] = websocket
                while True:
                    try:
                        message = await websocket.recv()
                        data = json.loads(message)
                        await callback(exchange, data)
                    except websockets.ConnectionClosed:
                        break

        except Exception as e:
            print(f"WebSocket connection error for {exchange}: {e}")

    async def subscribe_to_symbols(self, exchange: str, symbols: List[str], message_type: str = 'ticker'):
        """
        Subscribe to specific symbols for an exchange
        """
        subscription_message = {
            'type': 'subscribe',
            'product_ids': symbols,
            'channels': [message_type]
        }
        await self.connections[exchange].send(json.dumps(subscription_message))

    async def close_all_connections(self):
        """
        Close all active WebSocket connections
        """
        for exchange, connection in self.connections.items():
            await connection.close()