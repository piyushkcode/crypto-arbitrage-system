# backend/database/schemas/arbitrage_schema.py
from mongoengine import Document, StringField, FloatField, DateTimeField, BooleanField, ListField
from datetime import datetime

class ArbitrageOpportunity(Document):
    """
    Model to track and log arbitrage opportunities
    """
    symbol = StringField(required=True)
    
    # Exchanges involved
    source_exchange = StringField(required=True)
    destination_exchange = StringField(required=True)
    
    # Price details
    source_price = FloatField(required=True)
    destination_price = FloatField(required=True)
    
    # Profit calculation
    profit_percentage = FloatField(required=True)
    profit_amount = FloatField(required=True)
    
    # Trade execution details
    executed = BooleanField(default=False)
    execution_timestamp = DateTimeField()
    
    # Additional trade metadata
    trade_amount = FloatField()
    trade_fees = FloatField()
    
    # Risk and prediction details
    ml_prediction_confidence = FloatField()
    risk_score = FloatField()
    
    # Tracking
    created_at = DateTimeField(default=datetime.utcnow)
    
    meta = {
        'collection': 'arbitrage_opportunities',
        'indexes': [
            'symbol',
            'source_exchange',
            'destination_exchange',
            'executed',
            {'fields': ['created_at'], 'expireAfterSeconds': 2592000}  # Keep for 30 days
        ],
        'ordering': ['-created_at']
    }

    @classmethod
    def log_opportunity(cls, data):
        """
        Create and save a new arbitrage opportunity
        """
        opportunity = cls(**data)
        opportunity.save()
        return opportunity