from .base_exchange import BaseExchange
from typing import Dict, List

class KuCoinExchange(BaseExchange):
    def __init__(self, api_key: str = None, api_secret: str = None):
        super().__init__(api_key, api_secret)
        self.base_url = "https://api.kucoin.com/api/v1"

    def get_ticker_price(self, symbol: str) -> float:
        """Fetch current ticker price for a given symbol on KuCoin."""
        url = f"{self.base_url}/market/orderbook/level1"
        params = {"symbol": symbol}
        
        response = self._make_request(url, params)
        return float(response.get('data', {}).get('price', 0))

    def get_order_book(self, symbol: str) -> Dict[str, List[Dict[str, float]]]:
        """Fetch current order book for a given symbol on KuCoin."""
        url = f"{self.base_url}/market/orderbook/level2_20"
        params = {"symbol": symbol}
        
        response = self._make_request(url, params)
        data = response.get('data', {})
        
        return {
            "bids": [{"price": float(bid[0]), "quantity": float(bid[1])} for bid in data.get('bids', [])],
            "asks": [{"price": float(ask[0]), "quantity": float(ask[1])} for ask in data.get('asks', [])]
        }