
# backend/app/services/arbitrage_service.py
import asyncio
from typing import List, Dict
from .exchange_service import ExchangeService

class ArbitrageService:
    def __init__(self, exchanges: List[ExchangeService]):
        self.exchanges = exchanges

    async def detect_simple_arbitrage(self, symbol: str) -> List[Dict]:
        """
        Detect price differences for a given symbol across exchanges
        """
        prices = await asyncio.gather(
            *[exchange.get_price(symbol) for exchange in self.exchanges]
        )
        
        arbitrage_opportunities = []
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                price_diff_percentage = abs(prices[i] - prices[j]) / min(prices[i], prices[j]) * 100
                if price_diff_percentage > 1:  # 1% threshold
                    arbitrage_opportunities.append({
                        "symbol": symbol,
                        "exchange1": self.exchanges[i].name,
                        "exchange2": self.exchanges[j].name,
                        "price1": prices[i],
                        "price2": prices[j],
                        "profit_percentage": price_diff_percentage
                    })
        
        return arbitrage_opportunities

    async def detect_triangular_arbitrage(self, exchange):
        """
        Detect triangular arbitrage opportunities within a single exchange
        """
        # Implementation depends on specific exchange's trading pairs
        pass