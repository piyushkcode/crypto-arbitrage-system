# backend/app/services/machine_learning_service.py
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from typing import List, Dict

class MLArbitragePredictor:
    def __init__(self, historical_data: List[Dict]):
        self.data = pd.DataFrame(historical_data)
        self.model = None
        self.scaler = MinMaxScaler()

    def prepare_data(self, look_back: int = 60):
        # Prepare time series data for LSTM
        price_spreads = self.data['price_spread'].values
        X, y = [], []

        for i in range(len(price_spreads) - look_back):
            X.append(price_spreads[i:i+look_back])
            y.append(price_spreads[i+look_back])

        X = np.array(X)
        y = np.array(y)

        # Normalize the data
        X = self.scaler.fit_transform(X)
        y = self.scaler.transform(y.reshape(-1, 1))

        return train_test_split(X, y, test_size=0.2, random_state=42)

    def build_lstm_model(self, look_back: int = 60):
        model = Sequential([
            LSTM(50, activation='relu', input_shape=(look_back, 1), return_sequences=True),
            LSTM(50, activation='relu'),
            Dense(25, activation='relu'),
            Dense(1)
        ])
        model.compile(optimizer='adam', loss='mse')
        return model

    def train_model(self):
        X_train, X_test, y_train, y_test = self.prepare_data()
        X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
        X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))

        self.model = self.build_lstm_model()
        self.model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))

    def predict_arbitrage(self, current_data):
        if not self.model:
            raise ValueError("Model not trained. Call train_model() first.")
        
        # Prepare and scale input data
        scaled_data = self.scaler.transform(current_data)
        prediction = self.model.predict(scaled_data)
        
        # Inverse transform to get actual price spread prediction
        return self.scaler.inverse_transform(prediction)[0][0]