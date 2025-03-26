# backend/database/models/exchange_model.py
from datetime import datetime
from typing import Dict, Any, Optional

class ExchangeModel:
    """
    MongoDB Exchange Model for tracking exchange information
    """
    COLLECTION_NAME = 'exchanges'

    @classmethod
    def create(cls, name: str, api_key: str = None, api_secret: str = None) -> Dict[str, Any]:
        """
        Create a new exchange entry
        """
        from ..connection import MongoDBConnection
        
        exchange_data = {
            'name': name,
            'api_key': api_key,
            'api_secret': api_secret,
            'is_active': True,
            'total_trades': 0,
            'total_volume': 0.0,
            'last_sync_time': datetime.utcnow()
        }
        
        collection = MongoDBConnection().get_collection(cls.COLLECTION_NAME)
        result = collection.insert_one(exchange_data)
        
        exchange_data['_id'] = result.inserted_id
        return exchange_data

    @classmethod
    def get_by_name(cls, name: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve exchange by name
        """
        from ..connection import MongoDBConnection
        
        collection = MongoDBConnection().get_collection(cls.COLLECTION_NAME)
        return collection.find_one({'name': name})

    @classmethod
    def update_performance(cls, name: str, trades: int, volume: float) -> bool:
        """
        Update exchange performance metrics
        """
        from ..connection import MongoDBConnection
        
        collection = MongoDBConnection().get_collection(cls.COLLECTION_NAME)
        result = collection.update_one(
            {'name': name},
            {
                '$inc': {
                    'total_trades': trades,
                    'total_volume': volume
                },
                '$set': {
                    'last_sync_time': datetime.utcnow()
                }
            }
        )
        
        return result.modified_count > 0