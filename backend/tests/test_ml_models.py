import unittest
import numpy as np
import pandas as pd
from backend.machine_learning import LSTMArbitrageModel, RandomForestArbitrageModel

class TestArbitrageModels(unittest.TestCase):
    def setUp(self):
        # Generate synthetic price spread data
        np.random.seed(42)
        dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
        self.price_spreads = pd.DataFrame({
            'date': dates,
            'binance_price': np.random.normal(50000, 1000, len(dates)),
            'kraken_price': np.random.normal(50000, 1000, len(dates)),
            'spread': np.random.normal(0, 100, len(dates))
        })

    def test_lstm_model_training(self):
        """Test LSTM model training and prediction."""
        lstm_model = LSTMArbitrageModel(lookback=30, forecast_horizon=15)
        
        # Prepare data
        X, y = lstm_model.prepare_data(self.price_spreads[['spread']])
        
        # Split data
        train_size = int(0.8 * len(X))
        X_train, X_test = X[:train_size], X[train_size:]
        y_train, y_test = y[:train_size], y[train_size:]
        
        # Train model
        lstm_model.train(X_train, y_train, epochs=10)
        
        # Predict
        predictions = lstm_model.predict(X_test)
        
        self.assertEqual(predictions.shape, y_test.shape)
        self.assertFalse(np.allclose(predictions, 0))  # Check non-zero predictions

    def test_random_forest_model(self):
        """Test Random Forest model training and evaluation."""
        rf_model = RandomForestArbitrageModel(n_estimators=50)
        
        # Prepare data
        X_train, X_test, y_train, y_test = rf_model.prepare_data(
            self.price_spreads, 
            target_column='spread'
        )
        
        # Train model
        rf_model.train(X_train, y_train)
        
        # Evaluate model
        metrics = rf_model.evaluate(X_test, y_test)
        
        # Check metrics
        self.assertIn('mse', metrics)
        self.assertIn('mae', metrics)
        self.assertIn('rmse', metrics)
        
        # Predict new data
        new_data = X_test[:5]  # Use first 5 test samples
        predictions = rf_model.predict_arbitrage_opportunities(new_data)
        
        self.assertEqual(len(predictions), 5)
        self.assertFalse(np.allclose(predictions, 0))