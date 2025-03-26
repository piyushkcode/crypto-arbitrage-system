import abc
from typing import List, Dict, Any
import requests

class BaseExchange(abc.ABC):
    def __init__(self, api_key: str = None, api_secret: str = None):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = None

    @abc.abstractmethod
    def get_ticker_price(self, symbol: str) -> float:
        """Fetch current ticker price for a given symbol."""
        pass

    @abc.abstractmethod
    def get_order_book(self, symbol: str) -> Dict[str, List[Dict[str, float]]]:
        """Fetch current order book for a given symbol."""
        pass

    def _make_request(self, url: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """Generic method to make HTTP requests."""
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error making request: {e}")
            return {}