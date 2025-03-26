import axios from 'axios';

export const dashboardService = {
  async getDashboardData() {
    try {
      const response = await axios.get('/api/dashboard');
      return response.data;
    } catch (error) {
      console.error('Failed to fetch dashboard data', error);
      throw error;
    }
  },

  async getTopOpportunities() {
    try {
      const response = await axios.get('/api/dashboard/top-opportunities');
      return response.data;
    } catch (error) {
      console.error('Failed to fetch top opportunities', error);
      throw error;
    }
  }
};