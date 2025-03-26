import axios from 'axios';

export const walletService = {
  async getWalletBalance() {
    try {
      const response = await axios.get('/api/wallet/balance');
      return response.data;
    } catch (error) {
      console.error('Failed to fetch wallet balance', error);
      throw error;
    }
  },

  async getWalletDistribution() {
    try {
      const response = await axios.get('/api/wallet/distribution');
      return response.data;
    } catch (error) {
      console.error('Failed to fetch wallet distribution', error);
      throw error;
    }
  },

  async transferFunds(params: {
    from: string, 
    to: string, 
    amount: number, 
    currency: string
  }) {
    try {
      const response = await axios.post('/api/wallet/transfer', params);
      return response.data;
    } catch (error) {
      console.error('Failed to transfer funds', error);
      throw error;
    }
  }
};