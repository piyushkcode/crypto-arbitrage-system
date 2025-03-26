import React from 'react';
import { ArrowUpRightIcon } from 'lucide-react';

const opportunities = [
  { 
    pair: 'BTC/USDT', 
    exchanges: 'Binance → Kraken', 
    percentage: 0.87 
  },
  { 
    pair: 'ETH/BTC/XRP', 
    exchanges: 'Triangular (Binance)', 
    percentage: 0.74 
  },
  { 
    pair: 'SOL/USDT', 
    exchanges: 'KuCoin → OKX', 
    percentage: 0.61 
  }
];

const TopOpportunitiesTable = () => {
  return (
    <div className="bg-gray-900 rounded-lg p-4">
      <div className="flex justify-between items-center mb-4">
        <h3 className="text-white text-lg">Top Opportunities</h3>
        <div className="flex space-x-2">
          <button className="bg-blue-500 text-white px-3 py-1 rounded-lg text-sm">
            All
          </button>
          <button className="bg-gray-700 text-gray-400 px-3 py-1 rounded-lg text-sm">
            Custom
          </button>
        </div>
      </div>
      <div className="space-y-2">
        {opportunities.map((opp, index) => (
          <div 
            key={index} 
            className="bg-gray-800 p-3 rounded-lg flex items-center justify-between"
          >
            <div>
              <div className="text-white font-semibold">{opp.pair}</div>
              <div className="text-gray-400 text-sm">{opp.exchanges}</div>
            </div>
            <div className="flex items-center text-green-500">
              {opp.percentage}%
              <ArrowUpRightIcon className="ml-2" size={16} />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default TopOpportunitiesTable;