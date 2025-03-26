from .base_exchange import BaseExchange
from typing import Dict, List

class KrakenExchange(BaseExchange):
    def __init__(self, api_key: str = None, api_secret: str = None):
        super().__init__(api_key, api_secret)
        self.base_url = "https://api.kraken.com/0/public"

    def get_ticker_price(self, symbol: str) -> float:
        """Fetch current ticker price for a given symbol on Kraken."""
        url = f"{self.base_url}/Ticker"
        params = {"pair": symbol}
        
        response = self._make_request(url, params)
        pair_data = list(response.get('result', {}).values())[0] if response.get('result') else {}
        return float(pair_data.get('c', [0])[0])

    def get_order_book(self, symbol: str) -> Dict[str, List[Dict[str, float]]]:
        """Fetch current order book for a given symbol on Kraken."""
        url = f"{self.base_url}/Depth"
        params = {
            "pair": symbol,
            "count": 20  # Configurable limit
        }
        
        response = self._make_request(url, params)
        pair_data = list(response.get('result', {}).values())[0] if response.get('result') else {}
        
        return {
            "bids": [{"price": float(bid[0]), "quantity": float(bid[1])} for bid in pair_data.get('bids', [])],
            "asks": [{"price": float(ask[0]), "quantity": float(ask[1])} for ask in pair_data.get('asks', [])]
        }