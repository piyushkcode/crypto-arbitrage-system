# backend/database/schemas/exchange_schema.py
from mongoengine import Document, StringField, FloatField, DateTimeField, DictField
from datetime import datetime

class Exchange(Document):
    """
    Exchange model to track exchange-specific metadata and performance
    """
    name = StringField(required=True, unique=True)
    api_endpoint = StringField(required=True)
    
    # Trading Fees
    maker_fee = FloatField(default=0.001)  # 0.1%
    taker_fee = FloatField(default=0.002)  # 0.2%
    
    # Performance Metrics
    total_trades = FloatField(default=0)
    total_volume = FloatField(default=0)
    
    # API Connection Details (securely stored)
    connection_config = DictField()
    
    # Tracking timestamps
    last_sync = DateTimeField(default=datetime.utcnow)
    created_at = DateTimeField(default=datetime.utcnow)
    
    meta = {
        'collection': 'exchanges',
        'indexes': [
            'name',
            {'fields': ['last_sync'], 'expireAfterSeconds': 0}
        ]
    }

    def update_performance(self, trades, volume):
        """
        Update exchange performance metrics
        """
        self.total_trades += trades
        self.total_volume += volume
        self.last_sync = datetime.utcnow()
        self.save()