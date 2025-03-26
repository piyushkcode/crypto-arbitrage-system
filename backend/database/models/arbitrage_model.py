# backend/database/models/arbitrage_model.py
from bson import ObjectId
from datetime import datetime
from typing import Dict, Any, Optional

class ArbitrageModel:
    """
    MongoDB Arbitrage Model for tracking arbitrage opportunities
    """
    COLLECTION_NAME = 'arbitrage_attempts'

    @classmethod
    def create(cls, user_id: str, exchange_id: str, opportunity: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new arbitrage attempt entry
        """
        from ..connection import MongoDBConnection
        
        arbitrage_data = {
            'user_id': ObjectId(user_id),
            'exchange_id': ObjectId(exchange_id),
            'symbol': opportunity.get('symbol'),
            'source_exchange': opportunity.get('source_exchange'),
            'destination_exchange': opportunity.get('destination_exchange'),
            'source_price': opportunity.get('source_price'),
            'destination_price': opportunity.get('destination_price'),
            'profit_percentage': opportunity.get('profit_percentage'),
            'trade_amount': opportunity.get('trade_amount', 0),
            'status': opportunity.get('status', 'detected'),
            'additional_data': opportunity,
            'created_at': datetime.utcnow()
        }
        
        collection = MongoDBConnection().get_collection(cls.COLLECTION_NAME)
        result = collection.insert_one(arbitrage_data)
        
        arbitrage_data['_id'] = result.inserted_id
        return arbitrage_data

    @classmethod
    def get_user_arbitrage_attempts(cls, user_id: str) -> list:
        """
        Retrieve arbitrage attempts for a specific user
        """
        from ..connection import MongoDBConnection
        
        collection = MongoDBConnection().get_collection(cls.COLLECTION_NAME)
        return list(collection.find({'user_id': ObjectId(user_id)}))

    @classmethod
    def update_status(cls, arbitrage_id: str, status: str, additional_data: Dict[str, Any] = None) -> bool:
        """
        Update arbitrage attempt status
        """
        from ..connection import MongoDBConnection
        
        collection = MongoDBConnection().get_collection(cls.COLLECTION_NAME)
        update_data = {
            '$set': {
                'status': status,
                'updated_at': datetime.utcnow()
            }
        }
        
        if additional_data:
            update_data['$set'].update(additional_data)
        
        result = collection.update_one(
            {'_id': ObjectId(arbitrage_id)},
            update_data
        )
        
        return result.modified_count > 0