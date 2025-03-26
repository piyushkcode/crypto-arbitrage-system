import pandas as pd
import numpy as np
from typing import Tuple, List, Dict
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split

class DataPreprocessor:
    def __init__(self, scaling_method: str = 'minmax'):
        """
        Initialize data preprocessor
        
        :param scaling_method: 'minmax' or 'standard' scaling
        """
        self.scaling_method = scaling_method
        self.scalers = {}

    def load_data(self, file_path: str) -> pd.DataFrame:
        """
        Load data from various file formats
        
        :param file_path: Path to data file
        :return: Loaded DataFrame
        """
        try:
            # Support multiple file formats
            if file_path.endswith('.csv'):
                return pd.read_csv(file_path)
            elif file_path.endswith('.json'):
                return pd.read_json(file_path)
            elif file_path.endswith('.xlsx'):
                return pd.read_excel(file_path)
            else:
                raise ValueError(f"Unsupported file format: {file_path}")
        except Exception as e:
            print(f"Error loading data: {e}")
            return pd.DataFrame()

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Clean and prepare data for analysis
        
        :param df: Input DataFrame
        :return: Cleaned DataFrame
        """
        # Remove duplicate rows
        df = df.drop_duplicates()
        
        # Handle missing values
        df = df.fillna(method='ffill')  # Forward fill missing values
        
        # Remove infinite values
        df = df.replace([np.inf, -np.inf], np.nan).dropna()
        
        return df

    def extract_features(self, df: pd.DataFrame, 
                         price_columns: List[str], 
                         window_sizes: List[int] = [1, 5, 10]) -> pd.DataFrame:
        """
        Extract additional features from price data
        
        :param df: Input DataFrame
        :param price_columns: Columns containing price data
        :param window_sizes: Different window sizes for feature extraction
        :return: DataFrame with additional features
        """
        # Create a copy to avoid modifying original DataFrame
        features_df = df.copy()
        
        for col in price_columns:
            # Moving averages
            for window in window_sizes:
                features_df[f'{col}_ma_{window}'] = df[col].rolling(window=window).mean()
            
            # Price changes
            features_df[f'{col}_change'] = df[col].pct_change()
            
            # Volatility (standard deviation of returns)
            features_df[f'{col}_volatility'] = df[col].pct_change().rolling(window=10).std()
        
        # Drop rows with NaN created by feature engineering
        features_df = features_df.dropna()
        
        return features_df

    def scale_data(self, df: pd.DataFrame, columns: List[str]) -> Tuple[np.ndarray, Dict]:
        """
        Scale selected columns
        
        :param df: Input DataFrame
        :param columns: Columns to scale
        :return: Scaled data and scaler dictionary
        """
        # Select columns to scale
        X = df[columns].values
        
        # Choose scaling method
        if self.scaling_method == 'minmax':
            scaler = MinMaxScaler()
        else:
            scaler = StandardScaler()
        
        # Fit and transform
        X_scaled = scaler.fit_transform(X)
        
        # Store scaler for potential inverse transformation
        self.scalers[','.join(columns)] = scaler
        
        return X_scaled, {'scaler': scaler}

    def prepare_sequence_data(self, 
                               df: pd.DataFrame, 
                               target_column: str, 
                               lookback: int = 60, 
                               forecast_horizon: int = 15) -> Tuple[np.ndarray, np.ndarray]:
        """
        Prepare sequential data for time series models
        
        :param df: Input DataFrame
        :param target_column: Column to predict
        :param lookback: Number of past time steps
        :param forecast_horizon: Number of future time steps to predict
        :return: X (input sequences) and y (target sequences)
        """
        # Extract target column
        target_data = df[target_column].values
        
        # Create sequences
        X, y = [], []
        for i in range(len(target_data) - lookback - forecast_horizon + 1):
            X.append(target_data[i:i+lookback])
            y.append(target_data[i+lookback:i+lookback+forecast_horizon])
        
        return np.array(X), np.array(y)

    def split_data(self, X: np.ndarray, y: np.ndarray, test_size: float = 0.2) -> Tuple:
        """
        Split data into training and testing sets
        
        :param X: Input features
        :param y: Target values
        :param test_size: Proportion of data to use for testing
        :return: Train and test splits
        """
        return train_test_split(X, y, test_size=test_size, shuffle=False)