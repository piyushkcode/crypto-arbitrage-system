import React, { createContext, useState, useContext } from 'react';

interface DashboardContextType {
  totalProfit: number;
  currentOpportunities: number;
  newOpportunities: number;
  winRate: number;
  totalBalance: number;
  topOpportunities: Array<{
    pair: string;
    exchanges: string;
    percentage: number;
  }>;
}

const DashboardContext = createContext<DashboardContextType | undefined>(undefined);

export const DashboardProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [dashboardData] = useState<DashboardContextType>({
    totalProfit: 18724.53,
    currentOpportunities: 37,
    newOpportunities: 12,
    winRate: 94.3,
    totalBalance: 527392.15,
    topOpportunities: [
      { pair: 'BTC/USDT', exchanges: 'Binance → Kraken', percentage: 0.87 },
      { pair: 'ETH/BTC/XRP', exchanges: 'Triangular (Binance)', percentage: 0.74 },
      { pair: 'SOL/USDT', exchanges: 'KuCoin → OKX', percentage: 0.61 }
    ]
  });

  return (
    <DashboardContext.Provider value={dashboardData}>
      {children}
    </DashboardContext.Provider>
  );
};

export const useDashboard = () => {
  const context = useContext(DashboardContext);
  if (context === undefined) {
    throw new Error('useDashboard must be used within a DashboardProvider');
  }
  return context;
};