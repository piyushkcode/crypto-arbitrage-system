# backend/database/models/user_model.py
from bson import ObjectId
from datetime import datetime
import bcrypt
from typing import Optional, Dict, Any

class UserModel:
    """
    MongoDB User Model with authentication and management methods
    """
    COLLECTION_NAME = 'users'

    @classmethod
    def create(cls, username: str, email: str, password: str) -> Dict[str, Any]:
        """
        Create a new user
        """
        from ..connection import MongoDBConnection
        
        # Hash password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        user_data = {
            'username': username,
            'email': email,
            'hashed_password': hashed_password,
            'is_active': True,
            'is_admin': False,
            'balance': 0.0,
            'last_login': None,
            'created_at': datetime.utcnow()
        }
        
        collection = MongoDBConnection().get_collection(cls.COLLECTION_NAME)
        result = collection.insert_one(user_data)
        
        user_data['_id'] = result.inserted_id
        return user_data

    @classmethod
    def authenticate(cls, email: str, password: str) -> Optional[Dict[str, Any]]:
        """
        Authenticate user
        """
        from ..connection import MongoDBConnection
        
        collection = MongoDBConnection().get_collection(cls.COLLECTION_NAME)
        user = collection.find_one({'email': email})
        
        if user and bcrypt.checkpw(password.encode('utf-8'), user['hashed_password']):
            # Update last login
            collection.update_one(
                {'_id': user['_id']}, 
                {'$set': {'last_login': datetime.utcnow()}}
            )
            return user
        
        return None

    @classmethod
    def get_by_id(cls, user_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve user by ID
        """
        from ..connection import MongoDBConnection
        
        collection = MongoDBConnection().get_collection(cls.COLLECTION_NAME)
        return collection.find_one({'_id': ObjectId(user_id)})

    @classmethod
    def update(cls, user_id: str, update_data: Dict[str, Any]) -> bool:
        """
        Update user information
        """
        from ..connection import MongoDBConnection
        
        collection = MongoDBConnection().get_collection(cls.COLLECTION_NAME)
        result = collection.update_one(
            {'_id': ObjectId(user_id)}, 
            {'$set': update_data}
        )
        
        return result.modified_count > 0