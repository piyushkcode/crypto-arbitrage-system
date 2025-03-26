# backend/app/config/settings.py
import os
from typing import List, Dict, Any
from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    """
    Application configuration settings managed through environment variables
    """
    # Application Settings
    DEBUG: bool = Field(default=False, env='APP_DEBUG')
    SECRET_KEY: str = Field(default='default-secret-key', env='SECRET_KEY')
    
    # Arbitrage Settings
    ARBITRAGE_THRESHOLD: float = Field(default=1.5, env='ARBITRAGE_THRESHOLD')
    MAX_TRADE_AMOUNT: float = Field(default=1000, env='MAX_TRADE_AMOUNT')
    
    # Exchange API Configurations
    EXCHANGES: List[str] = Field(
        default=['binance', 'kraken', 'kucoin'], 
        env='SUPPORTED_EXCHANGES'
    )
    
    # API Keys (use with caution, prefer environment variables)
    EXCHANGE_API_KEYS: Dict[str, Dict[str, str]] = {
        'binance': {
            'api_key': os.getenv('BINANCE_API_KEY', ''),
            'secret_key': os.getenv('BINANCE_SECRET_KEY', '')
        },
        'kraken': {
            'api_key': os.getenv('KRAKEN_API_KEY', ''),
            'secret_key': os.getenv('KRAKEN_SECRET_KEY', '')
        },
        'kucoin': {
            'api_key': os.getenv('KUCOIN_API_KEY', ''),
            'secret_key': os.getenv('KUCOIN_SECRET_KEY', '')
        }
    }
    
    # Machine Learning Settings
    ML_MODEL_PATH: str = Field(
        default='models/arbitrage_predictor.pkl', 
        env='ML_MODEL_PATH'
    )
    
    # Database Configuration
    DATABASE_URL: str = Field(
        default='postgresql://user:pass@localhost/crypto_arbitrage', 
        env='DATABASE_URL'
    )
    
    # WebSocket Settings
    WEBSOCKET_TIMEOUT: int = Field(default=30, env='WEBSOCKET_TIMEOUT')
    
    # Logging Configuration
    LOG_LEVEL: str = Field(default='INFO', env='LOG_LEVEL')
    
    class Config:
        # Allow case-sensitive environment variable names
        case_sensitive = True
        
        # Optionally load from a .env file
        env_file = '.env'
        env_file_encoding = 'utf-8'

    def get_exchange_config(self, exchange: str) -> Dict[str, str]:
        """
        Retrieve API configuration for a specific exchange
        """
        return self.EXCHANGE_API_KEYS.get(exchange, {})

# Create a singleton instance of Settings
settings = Settings()