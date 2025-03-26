# backend/app/utils/api_client.py
import ccxt
from typing import Dict, Any

def create_exchange_client(exchange_id: str, config: Dict[str, Any] = None) -> Any:
    """
    Create and return an exchange client with optional configuration
    """
    default_config = {
        'enableRateLimit': True,
        'timeout': 10000
    }
    
    if config:
        default_config.update(config)
    
    try:
        exchange_class = getattr(ccxt, exchange_id)
        return exchange_class(default_config)
    except AttributeError:
        raise ValueError(f"Exchange {exchange_id} not supported")