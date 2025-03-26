import React from 'react';
import SummaryCards from '../components/Dashboard/SummaryCards';
import PerformanceChart from '../components/Dashboard/PerformanceChart';
import TopOpportunitiesTable from '../components/Dashboard/TopOpportunitiesTable';
import WalletDistributionChart from '../components/Dashboard/WalletDistributionChart';
import AIMarketPredictions from '../components/Dashboard/AIMarketPredictions';
import AnalyticsCompliance from '../components/Dashboard/AnalyticsCompliance';

const performanceData = [
  { 
    time: '00:00', 
    simple: 0, 
    triangular: 0, 
    statistical: 0 
  },
  { 
    time: '03:00', 
    simple: 0.5, 
    triangular: 0.4, 
    statistical: 0.3 
  },
  { 
    time: '06:00', 
    simple: 1.2, 
    triangular: 1.0, 
    statistical: 0.8 
  },
  { 
    time: '09:00', 
    simple: 1.8, 
    triangular: 1.6, 
    statistical: 1.4 
  },
  { 
    time: '12:00', 
    simple: 2.3, 
    triangular: 2.1, 
    statistical: 1.9 
  },
  { 
    time: '15:00', 
    simple: 2.7, 
    triangular: 2.5, 
    statistical: 2.3 
  },
  { 
    time: '18:00', 
    simple: 2.9, 
    triangular: 2.7, 
    statistical: 2.5 
  },
  { 
    time: '21:00', 
    simple: 3.0, 
    triangular: 2.8, 
    statistical: 2.6 
  }
];

const Dashboard = () => {
  return (
    <div className="space-y-6">
      <SummaryCards />
      
      <div className="grid grid-cols-3 gap-6">
        <div className="col-span-2">
          <PerformanceChart data={performanceData} />
        </div>
        <TopOpportunitiesTable />
      </div>
      
      <div className="grid grid-cols-3 gap-6">
        <WalletDistributionChart />
        <AIMarketPredictions />
        <AnalyticsCompliance />
      </div>
    </div>
  );
};

export default Dashboard;