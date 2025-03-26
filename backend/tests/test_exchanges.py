import unittest
from backend.exchanges import BinanceExchange, KrakenExchange, KuCoinExchange

class TestExchangeIntegration(unittest.TestCase):
    def setUp(self):
        self.exchanges = {
            'binance': BinanceExchange(),
            'kraken': KrakenExchange(),
            'kucoin': KuCoinExchange()
        }
        self.test_symbols = {
            'binance': 'BTCUSDT',
            'kraken': 'XBTUSD',
            'kucoin': 'BTC-USDT'
        }

    def test_ticker_price_retrieval(self):
        """Test retrieving ticker prices from different exchanges."""
        for exchange_name, exchange in self.exchanges.items():
            with self.subTest(exchange=exchange_name):
                symbol = self.test_symbols[exchange_name]
                price = exchange.get_ticker_price(symbol)
                
                self.assertIsNotNone(price)
                self.assertGreater(price, 0)

    def test_order_book_retrieval(self):
        """Test retrieving order books from different exchanges."""
        for exchange_name, exchange in self.exchanges.items():
            with self.subTest(exchange=exchange_name):
                symbol = self.test_symbols[exchange_name]
                order_book = exchange.get_order_book(symbol)
                
                self.assertIn('bids', order_book)
                self.assertIn('asks', order_book)
                
                self.assertTrue(len(order_book['bids']) > 0)
                self.assertTrue(len(order_book['asks']) > 0)
                
                # Check bid and ask structures
                for side in ['bids', 'asks']:
                    for entry in order_book[side]:
                        self.assertIn('price', entry)
                        self.assertIn('quantity', entry)
                        self.assertGreater(entry['price'], 0)
                        self.assertGreater(entry['quantity'], 0)