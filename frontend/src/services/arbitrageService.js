import axios from 'axios';

export const arbitrageService = {
  async getOpportunities() {
    try {
      const response = await axios.get('/api/arbitrage/opportunities');
      return response.data;
    } catch (error) {
      console.error('Failed to fetch arbitrage opportunities', error);
      throw error;
    }
  },

  async executeArbitrage(opportunityId: string) {
    try {
      const response = await axios.post('/api/arbitrage/execute', { opportunityId });
      return response.data;
    } catch (error) {
      console.error('Failed to execute arbitrage', error);
      throw error;
    }
  },

  async getPerformanceHistory() {
    try {
      const response = await axios.get('/api/arbitrage/performance');
      return response.data;
    } catch (error) {
      console.error('Failed to fetch performance history', error);
      throw error;
    }
  }
};