# backend/app/services/exchange_service.py
import ccxt
import asyncio
from typing import Dict, Any

class ExchangeService:
    def __init__(self, exchange_id: str):
        self.name = exchange_id
        self.exchange = getattr(ccxt, exchange_id)({
            'enableRateLimit': True,
            'timeout': 10000
        })

    async def fetch_ticker(self, symbol: str) -> Dict[str, Any]:
        try:
            return await self.exchange.fetch_ticker(symbol)
        except Exception as e:
            print(f"Error fetching ticker for {symbol} on {self.name}: {e}")
            return None

    async def get_price(self, symbol: str) -> float:
        ticker = await self.fetch_ticker(symbol)
        return ticker['last'] if ticker else None

    async def create_order(self, symbol: str, type: str, side: str, amount: float, price: float = None):
        try:
            return await self.exchange.create_order(symbol, type, side, amount, price)
        except Exception as e:
            print(f"Order creation error on {self.name}: {e}")
            return None