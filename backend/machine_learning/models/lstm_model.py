import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from typing import Tuple

class LSTMArbitrageModel:
    def __init__(self, lookback: int = 60, forecast_horizon: int = 15):
        """
        Initialize LSTM model for arbitrage prediction
        
        :param lookback: Number of past time steps to use for prediction
        :param forecast_horizon: Number of future time steps to predict
        """
        self.lookback = lookback
        self.forecast_horizon = forecast_horizon
        self.model = None
        self.scaler = MinMaxScaler()

    def prepare_data(self, price_spreads: pd.DataFrame) -> Tuple[np.ndarray, np.ndarray]:
        """
        Prepare data for LSTM model training
        
        :param price_spreads: DataFrame with price spread data
        :return: Prepared X and y data for training
        """
        # Normalize the data
        scaled_data = self.scaler.fit_transform(price_spreads)
        
        # Create sequences
        X, y = [], []
        for i in range(len(scaled_data) - self.lookback - self.forecast_horizon + 1):
            X.append(scaled_data[i:i+self.lookback])
            y.append(scaled_data[i+self.lookback:i+self.lookback+self.forecast_horizon, 0])
        
        return np.array(X), np.array(y)

    def build_model(self, input_shape: Tuple[int, int]):
        """
        Build LSTM model architecture
        
        :param input_shape: Shape of input data
        """
        self.model = Sequential([
            LSTM(50, activation='relu', input_shape=input_shape, return_sequences=True),
            LSTM(50, activation='relu'),
            Dense(self.forecast_horizon)
        ])
        
        self.model.compile(optimizer='adam', loss='mse')

    def train(self, X_train: np.ndarray, y_train: np.ndarray, epochs: int = 50, batch_size: int = 32):
        """
        Train the LSTM model
        
        :param X_train: Training input data
        :param y_train: Training target data
        :param epochs: Number of training epochs
        :param batch_size: Batch size for training
        """
        if self.model is None:
            self.build_model(input_shape=(X_train.shape[1], X_train.shape[2]))
        
        self.model.fit(
            X_train, y_train, 
            epochs=epochs, 
            batch_size=batch_size, 
            validation_split=0.2,
            verbose=1
        )

    def predict(self, X_test: np.ndarray) -> np.ndarray:
        """
        Make predictions using the trained model
        
        :param X_test: Test input data
        :return: Predicted price spreads
        """
        predictions = self.model.predict(X_test)
        return self.scaler.inverse_transform(predictions)