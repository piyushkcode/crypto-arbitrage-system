import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error

class RandomForestArbitrageModel:
    def __init__(self, n_estimators: int = 100, random_state: int = 42):
        """
        Initialize Random Forest model for arbitrage prediction
        
        :param n_estimators: Number of trees in the forest
        :param random_state: Random seed for reproducibility
        """
        self.model = RandomForestRegressor(
            n_estimators=n_estimators, 
            random_state=random_state
        )
        self.scaler = StandardScaler()
        self.feature_columns = None

    def prepare_data(self, price_data: pd.DataFrame, target_column: str):
        """
        Prepare data for Random Forest model
        
        :param price_data: DataFrame with price and spread data
        :param target_column: Column to predict
        """
        # Select features (exclude target)
        self.feature_columns = [col for col in price_data.columns if col != target_column]
        
        X = price_data[self.feature_columns]
        y = price_data[target_column]
        
        # Scale features
        X_scaled = self.scaler.fit_transform(X)
        
        return train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    def train(self, X_train: np.ndarray, y_train: np.ndarray):
        """
        Train the Random Forest model
        
        :param X_train: Training input data
        :param y_train: Training target data
        """
        self.model.fit(X_train, y_train)

    def evaluate(self, X_test: np.ndarray, y_test: np.ndarray) -> dict:
        """
        Evaluate model performance
        
        :param X_test: Test input data
        :param y_test: Test target data
        :return: Dictionary of performance metrics
        """
        y_pred = self.model.predict(X_test)
        
        return {
            'mse': mean_squared_error(y_test, y_pred),
            'mae': mean_absolute_error(y_test, y_pred),
            'rmse': np.sqrt(mean_squared_error(y_test, y_pred))
        }

    def predict_arbitrage_opportunities(self, X_new: np.ndarray) -> np.ndarray:
        """
        Predict potential arbitrage opportunities
        
        :param X_new: New data for prediction
        :return: Predicted price spreads or arbitrage potential
        """
        # Scale new data using the same scaler
        X_scaled = self.scaler.transform(X_new)
        return self.model.predict(X_scaled)