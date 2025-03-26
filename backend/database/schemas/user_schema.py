# backend/database/schemas/user_schema.py
from mongoengine import Document, StringField, EmailField, DateTimeField, BooleanField
from datetime import datetime
import uuid

class User(Document):
    """
    User model for authentication and profile management
    """
    id = StringField(primary_key=True, default=lambda: str(uuid.uuid4()))
    username = StringField(required=True, unique=True, max_length=50)
    email = EmailField(required=True, unique=True)
    password_hash = StringField(required=True)
    is_active = BooleanField(default=True)
    is_verified = BooleanField(default=False)
    
    # API Key Management
    api_keys = StringField()  # Encrypted API keys for exchanges
    
    created_at = DateTimeField(default=datetime.utcnow)
    last_login = DateTimeField()
    
    meta = {
        'collection': 'users',
        'indexes': [
            'username',
            'email',
            {'fields': ['created_at'], 'expireAfterSeconds': 0}
        ]
    }

    def to_dict(self):
        """
        Convert user document to dictionary, excluding sensitive fields
        """
        return {
            'id': str(self.id),
            'username': self.username,
            'email': self.email,
            'is_active': self.is_active,
            'is_verified': self.is_verified,
            'created_at': self.created_at
        }