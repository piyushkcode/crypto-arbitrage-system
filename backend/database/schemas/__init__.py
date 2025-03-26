# backend/database/schemas/__init__.py
from .user_schema import User
from .exchange_schema import Exchange
from .arbitrage_schema import ArbitrageOpportunity
from .trade_schema import Trade

__all__ = [
    'User', 
    'Exchange', 
    'ArbitrageOpportunity', 
    'Trade'
]