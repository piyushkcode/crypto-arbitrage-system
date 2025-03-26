export const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:5000/api';

export const EXCHANGES = [
  'Binance',
  'Kraken',
  'KuCoin',
  'Coinbase',
  'Bitstamp'
];

export const ARBITRAGE_TYPES = [
  'Simple',
  'Triangular',
  'Statistical'
];

export const TRADE_STATUSES = {
  PENDING: 'Pending',
  EXECUTED: 'Executed',
  FAILED: 'Failed'
};