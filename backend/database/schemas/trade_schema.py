# backend/database/schemas/trade_schema.py
from mongoengine import Document, StringField, FloatField, DateTimeField, BooleanField
from datetime import datetime

class Trade(Document):
    """
    Model to track individual trades executed by the system
    """
    user_id = StringField(required=True)
    symbol = StringField(required=True)
    
    # Exchange details
    exchange = StringField(required=True)
    
    # Trade specifics
    trade_type = StringField(choices=['buy', 'sell'], required=True)
    amount = FloatField(required=True)
    price = FloatField(required=True)
    
    # Execution status
    status = StringField(
        choices=['pending', 'completed', 'failed'], 
        default='pending'
    )
    
    # Fees and totals
    fee = FloatField(default=0)
    total_cost = FloatField(required=True)
    
    # Timestamps
    created_at = DateTimeField(default=datetime.utcnow)
    executed_at = DateTimeField()
    
    # Arbitrage-specific details
    is_arbitrage = BooleanField(default=False)
    arbitrage_opportunity_id = StringField()
    
    meta = {
        'collection': 'trades',
        'indexes': [
            'user_id',
            'symbol',
            'exchange',
            'status',
            {'fields': ['created_at'], 'expireAfterSeconds': 5184000}  # Keep for 60 days
        ],
        'ordering': ['-created_at']
    }

    def mark_completed(self, execution_details):
        """
        Update trade status to completed
        """
        self.status = 'completed'
        self.executed_at = datetime.utcnow()
        self.fee = execution_details.get('fee', 0)
        self.save()

    def mark_failed(self, error_message):
        """
        Mark trade as failed
        """
        self.status = 'failed'
        self.save()