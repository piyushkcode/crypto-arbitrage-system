import os
import logging
import numpy as np
import pandas as pd
from typing import Dict, Any

from backend.machine_learning.models import LSTMArbitrageModel, RandomForestArbitrageModel
from backend.machine_learning.data_preprocessing import DataPreprocessor

class TrainingPipeline:
    def __init__(self, 
                 data_path: str, 
                 model_type: str = 'lstm', 
                 config: Dict[str, Any] = None):
        """
        Initialize training pipeline
        
        :param data_path: Path to input data file
        :param model_type: Type of model to train ('lstm' or 'random_forest')
        :param config: Configuration dictionary for training
        """
        # Setup logging
        logging.basicConfig(
            level=logging.INFO, 
            format='%(asctime)s - %(levelname)s: %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        
        # Default configuration
        self.config = {
            'test_size': 0.2,
            'lookback': 60,
            'forecast_horizon': 15,
            'epochs': 50,
            'batch_size': 32,
            'price_columns': ['binance_price', 'kraken_price'],
            'target_column': 'spread'
        }
        
        # Update with provided configuration
        if config:
            self.config.update(config)
        
        self.data_path = data_path
        self.model_type = model_type
        self.preprocessor = DataPreprocessor()
        self.model = None
    
    def prepare_data(self) -> Tuple[np.ndarray, np.ndarray]:
        """
        Prepare data for model training
        
        :return: Prepared input and target data
        """
        self.logger.info("Loading and preprocessing data...")
        
        # Load data
        raw_data = self.preprocessor.load_data(self.data_path)
        
        # Clean data
        cleaned_data = self.preprocessor.clean_data(raw_data)
        
        # Extract features
        featured_data = self.preprocessor.extract_features(
            cleaned_data, 
            self.config['price_columns']
        )
        
        # Prepare sequence data
        X, y = self.preprocessor.prepare_sequence_data(
            featured_data, 
            self.config['target_column'],
            lookback=self.config['lookback'],
            forecast_horizon=self.config['forecast_horizon']
        )
        
        return X, y
    
    def train_model(self, X: np.ndarray, y: np.ndarray):
        """
        Train the selected model
        
        :param X: Input training data
        :param y: Target training data
        """
        # Split data
        X_train, X_test, y_train, y_test = self.preprocessor.split_data(
            X, y, 
            test_size=self.config['test_size']
        )
        
        self.logger.info(f"Training {self.model_type.upper()} model...")
        
        if self.model_type == 'lstm':
            self.model = LSTMArbitrageModel(
                lookback=self.config['lookback'], 
                forecast_horizon=self.config['forecast_horizon']
            )
            self.model.train(
                X_train, y_train, 
                epochs=self.config['epochs'], 
                batch_size=self.config['batch_size']
            )
        
        elif self.model_type == 'random_forest':
            self.model = RandomForestArbitrageModel()
            self.model.train(X_train, y_train)
        
        else:
            raise ValueError(f"Unsupported model type: {self.model_type}")
        
        self.logger.info("Model training completed.")
    
    def evaluate_model(self, X: np.ndarray, y: np.ndarray) -> Dict[str, float]:
        """
        Evaluate model performance
        
        :param X: Input test data
        :param y: Target test data
        :return: Performance metrics
        """
        if self.model is None:
            raise ValueError("Model not trained. Call train_model first.")
        
        # Split data
        X_train, X_test, y_train, y_test = self.preprocessor.split_data(
            X, y, 
            test_size=self.config['test_size']
        )
        
        self.logger.info("Evaluating model performance...")
        
        if self.model_type == 'lstm':
            predictions = self.model.predict(X_test)
            mse = np.mean((predictions - y_test) ** 2)
            return {'mse': mse}
        
        elif self.model_type == 'random_forest':
            return self.model.evaluate(X_test, y_test)
    
    def save_model(self, save_dir: str = 'models'):
        """
        Save trained model
        
        :param save_dir: Directory to save model
        """
        if self.model is None:
            raise ValueError("No model to save. Train a model first.")
        
        # Create directory if it doesn't exist
        os.makedirs(save_dir, exist_ok=True)
        
        # Save based on model type
        model_filename = f"{self.model_type}_arbitrage_model.pkl"
        model_path = os.path.join(save_dir, model_filename)
        
        try:
            import joblib
            joblib.dump(self.model, model_path)
            self.logger.info(f"Model saved to {model_path}")
        except Exception as e:
            self.logger.error(f"Error saving model: {e}")
    
    def run_pipeline(self):
        """
        Execute complete training pipeline
        """
        try:
            # Prepare data
            X, y = self.prepare_data()
            
            # Train model
            self.train_model(X, y)
            
            # Evaluate model
            metrics = self.evaluate_model(X, y)
            self.logger.info(f"Model Performance Metrics: {metrics}")
            
            # Save model
            self.save_model()
            
        except Exception as e:
            self.logger.error(f"Pipeline execution failed: {e}")
            raise