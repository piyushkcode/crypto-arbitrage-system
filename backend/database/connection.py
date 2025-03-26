# backend/database/connection.py
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os
from dotenv import load_dotenv

class MongoDBConnection:
    """
    Singleton MongoDB connection manager
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MongoDBConnection, cls).__new__(cls)
            cls._connect()
        return cls._instance

    @classmethod
    def _connect(cls):
        """
        Establish MongoDB connection
        """
        # Load environment variables
        load_dotenv()

        # Get connection parameters
        MONGO_URI = os.getenv(
            'MONGO_URI', 
            'mongodb://localhost:27017/crypto_arbitrage'
        )
        
        try:
            # Create MongoDB client
            cls.client = MongoClient(MONGO_URI)
            
            # Extract database name from URI
            cls.database_name = MONGO_URI.split('/')[-1]
            
            # Verify connection
            cls.client.admin.command('ismaster')
            
            # Get database instance
            cls.db = cls.client[cls.database_name]
            
            print(f"Connected to MongoDB database: {cls.database_name}")
        
        except ConnectionFailure as e:
            print(f"Failed to connect to MongoDB: {e}")
            raise

    @classmethod
    def get_database(cls):
        """
        Get the database instance
        """
        if not hasattr(cls, 'db'):
            cls._connect()
        return cls.db

    @classmethod
    def get_collection(cls, collection_name):
        """
        Get a specific collection
        """
        return cls.get_database()[collection_name]

    def close(self):
        """
        Close the MongoDB connection
        """
        if hasattr(self, 'client'):
            self.client.close()