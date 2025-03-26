from .base_exchange import BaseExchange
from typing import Dict, List

class BinanceExchange(BaseExchange):
    def __init__(self, api_key: str = None, api_secret: str = None):
        super().__init__(api_key, api_secret)
        self.base_url = "https://api.binance.com/api/v3"

    def get_ticker_price(self, symbol: str) -> float:
        """Fetch current ticker price for a given symbol on Binance."""
        url = f"{self.base_url}/ticker/price"
        params = {"symbol": symbol}
        
        response = self._make_request(url, params)
        return float(response.get('price', 0))

    def get_order_book(self, symbol: str) -> Dict[str, List[Dict[str, float]]]:
        """Fetch current order book for a given symbol on Binance."""
        url = f"{self.base_url}/depth"
        params = {
            "symbol": symbol,
            "limit": 20  # Configurable limit
        }
        
        response = self._make_request(url, params)
        return {
            "bids": [{"price": float(bid[0]), "quantity": float(bid[1])} for bid in response.get('bids', [])],
            "asks": [{"price": float(ask[0]), "quantity": float(ask[1])} for ask in response.get('asks', [])]
        }