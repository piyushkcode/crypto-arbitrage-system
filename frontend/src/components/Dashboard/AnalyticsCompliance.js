import React from 'react';
import { ShieldCheckIcon, TrendingUpIcon } from 'lucide-react';

const AnalyticsCompliance = () => {
  return (
    <div className="bg-gray-900 rounded-lg p-4 h-full">
      <h3 className="text-white text-lg mb-4">Analytics Compliance</h3>
      <div className="space-y-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center">
            <ShieldCheckIcon className="text-green-500 mr-3" size={24} />
            <div>
              <div className="text-white font-semibold">Sharpe Ratio</div>
              <div className="text-gray-400 text-sm">Performance Metric</div>
            </div>
          </div>
          <div className="text-green-500 font-bold">3.24</div>
        </div>
        <div className="flex items-center justify-between">
          <div className="flex items-center">
            <TrendingUpIcon className="text-yellow-500 mr-3" size={24} />
            <div>
              <div className="text-white font-semibold">Risk Exposure</div>
              <div className="text-gray-400 text-sm">Portfolio Risk</div>
            </div>
          </div>
          <div className="text-yellow-500 font-bold">LOW</div>
        </div>
        <div className="flex items-center justify-between">
          <div className="flex items-center">
            <ShieldCheckIcon className="text-blue-500 mr-3" size={24} />
            <div>
              <div className="text-white font-semibold">Tax Compliance</div>
              <div className="text-gray-400 text-sm">Reporting Status</div>
            </div>
          </div>
          <div className="text-blue-500 font-bold">Up to date</div>
        </div>
      </div>
    </div>
  );
};

export default AnalyticsCompliance;