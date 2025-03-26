# backend/app/services/trading_service.py
from .arbitrage_service import ArbitrageService
from .machine_learning_service import MLArbitragePredictor
from .exchange_service import ExchangeService
import logging

class TradingService:
    def __init__(self, exchanges: list, ml_predictor: MLArbitragePredictor):
        self.exchanges = exchanges
        self.arbitrage_service = ArbitrageService(exchanges)
        self.ml_predictor = ml_predictor
        self.logger = logging.getLogger(__name__)

    async def execute_arbitrage_trade(self, arbitrage_opportunity):
        try:
            # Risk management checks
            if not self._check_trade_conditions(arbitrage_opportunity):
                return False

            # Execute buy and sell orders
            buy_exchange = arbitrage_opportunity['exchange1']
            sell_exchange = arbitrage_opportunity['exchange2']
            symbol = arbitrage_opportunity['symbol']
            amount = self._calculate_trade_amount(arbitrage_opportunity)

            buy_order = await buy_exchange.create_order(
                symbol, 'market', 'buy', amount, 
                arbitrage_opportunity['price1']
            )
            
            sell_order = await sell_exchange.create_order(
                symbol, 'market', 'sell', amount, 
                arbitrage_opportunity['price2']
            )

            self.logger.info(f"Arbitrage trade executed: {arbitrage_opportunity}")
            return True

        except Exception as e:
            self.logger.error(f"Arbitrage trade failed: {e}")
            return False

    def _check_trade_conditions(self, opportunity):
        # Implement risk management checks
        min_profit_threshold = 1.5  # 1.5% minimum profit
        max_trade_amount = 1000  # USD equivalent
        
        return (
            opportunity['profit_percentage'] > min_profit_threshold and
            self._check_liquidity(opportunity)
        )

    def _check_liquidity(self, opportunity):
        # Check if exchanges have sufficient liquidity
        # Implement actual liquidity check logic
        return True

    def _calculate_trade_amount(self, opportunity):
        # Calculate optimal trade amount based on opportunity and risk
        return min(1000, opportunity['profit_percentage'] * 10)