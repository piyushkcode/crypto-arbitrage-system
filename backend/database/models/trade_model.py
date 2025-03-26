# backend/database/models/trade_model.py
from bson import ObjectId
from datetime import datetime
from typing import Dict, Any, Optional

class TradeModel:
    """
    MongoDB Trade Model for tracking individual trades
    """
    COLLECTION_NAME = 'trades'

    @classmethod
    def create(cls, user_id: str, exchange_id: str, trade_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new trade entry
        """
        from ..connection import MongoDBConnection
        
        full_trade_data = {
            'user_id': ObjectId(user_id),
            'exchange_id': ObjectId(exchange_id),
            'symbol': trade_data.get('symbol'),
            'trade_type': trade_data.get('trade_type', 'buy'),
            'amount': trade_data.get('amount'),
            'price': trade_data.get('price'),
            'profit': trade_data.get('profit', 0.0),
            'fee': trade_data.get('fee', 0.0),
            'status': trade_data.get('status', 'pending'),
            'created_at': datetime.utcnow(),
            'updated_at': datetime.utcnow()
        }
        
        collection = MongoDBConnection().get_collection(cls.COLLECTION_NAME)
        result = collection.insert_one(full_trade_data)
        
        full_trade_data['_id'] = result.inserted_id
        return full_trade_data

    @classmethod
    def get_user_trades(cls, user_id: str) -> list:
        """
        Retrieve all trades for a specific user
        """
        from ..connection import MongoDBConnection
        
        collection = MongoDBConnection().get_collection(cls.COLLECTION_NAME)
        return list(collection.find({'user_id': ObjectId(user_id)}))

    @classmethod
    def update_trade_status(cls, trade_id: str, status: str, additional_data: Dict[str, Any] = None) -> bool:
        """
        Update trade status and optionally additional information
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
            {'_id': ObjectId(trade_id)},
            update_data
        )
        
        return result.modified_count > 0