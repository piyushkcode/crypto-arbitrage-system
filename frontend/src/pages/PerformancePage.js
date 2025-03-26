import React, { useState, useEffect } from 'react';
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';

interface PerformanceMetric {
  date: string;
  totalProfit: number;
  winRate: number;
  avgTradeProfit: number;
  totalTrades: number;
}

const PerformancePage: React.FC = () => {
  const [performanceData, setPerformanceData] = useState<PerformanceMetric[]>([]);
  const [timeframe, setTimeframe] = useState<'1D' | '1W' | '1M' | '3M'>('1W');

  const fetchPerformanceData = async () => {
    try {
      // Simulate API call with mock data
      const mockData: PerformanceMetric[] = [
        { 
          date: '2025-03-20', 
          totalProfit: 1245.67, 
          winRate: 92.5, 
          avgTradeProfit: 87.54, 
          totalTrades: 42 
        },
        { 
          date: '2025-03-21', 
          totalProfit: 1387.92, 
          winRate: 93.2, 
          avgTradeProfit: 92.13, 
          totalTrades: 47 
        },
        // More mock data points...
      ];

      setPerformanceData(mockData);
    } catch (error) {
      console.error('Failed to fetch performance data', error);
    }
  };

  useEffect(() => {
    fetchPerformanceData();
  }, [timeframe]);

  const timeframes = ['1D', '1W', '1M', '3M'];

  return (
    <div className="p-4 space-y-6">
      <h1 className="text-2xl font-bold mb-4">Performance Analytics</h1>

      <div className="grid grid-cols-4 gap-4 mb-6">
        {/* Performance Summary Cards */}
        <div className="bg-gray-100 p-4 rounded-lg">
          <h3 className="text-gray-600">Total Profit</h3>
          <p className="text-2xl font-bold text-green-600">
            ${performanceData.length > 0 
              ? performanceData[performanceData.length - 1].totalProfit.toLocaleString() 
              : '0'}
          </p>
        </div>
        <div className="bg-gray-100 p-4 rounded-lg">
          <h3 className="text-gray-600">Win Rate</h3>
          <p className="text-2xl font-bold text-blue-600">
            {performanceData.length > 0 
              ? `${performanceData[performanceData.length - 1].winRate}%`
              : '0%'}
          </p>
        </div>
        <div className="bg-gray-100 p-4 rounded-lg">
          <h3 className="text-gray-600">Avg Trade Profit</h3>
          <p className="text-2xl font-bold text-purple-600">
            ${performanceData.length > 0 
              ? performanceData[performanceData.length - 1].avgTradeProfit.toFixed(2)
              : '0.00'}
          </p>
        </div>
        <div className="bg-gray-100 p-4 rounded-lg">
          <h3 className="text-gray-600">Total Trades</h3>
          <p className="text-2xl font-bold text-indigo-600">
            {performanceData.length > 0 
              ? performanceData[performanceData.length - 1].totalTrades
              : '0'}
          </p>
        </div>
      </div>

      <div className="bg-gray-100 p-4 rounded-lg">
        <div className="flex justify-between items-center mb-4">
          <h2 className="text-xl font-semibold">Performance Trend</h2>
          <div className="space-x-2">
            {timeframes.map((tf) => (
              <button
                key={tf}
                className={`
                  px-3 py-1 rounded
                  ${timeframe === tf 
                    ? 'bg-blue-500 text-white' 
                    : 'bg-white text-blue-500 border border-blue-500'}
                `}
                onClick={() => setTimeframe(tf as '1D' | '1W' | '1M' | '3M')}
              >
                {tf}
              </button>
            ))}
          </div>
        </div>

        <ResponsiveContainer width="100%" height={300}>
          <LineChart data={performanceData}>
            <XAxis dataKey="date" />
            <YAxis />
            <Tooltip />
            <Line 
              type="monotone" 
              dataKey="totalProfit" 
              stroke="#8884d8" 
              strokeWidth={2}
            />
          </LineChart>
        </ResponsiveContainer>
      </div>

      <div className="bg-gray-100 p-4 rounded-lg">
        <h2 className="text-xl font-semibold mb-4">Detailed Performance Log</h2>
        <table className="w-full">
          <thead>
            <tr className="bg-white">
              <th className="p-2 text-left">Date</th>
              <th className="p-2 text-right">Total Profit</th>
              <th className="p-2 text-right">Win Rate</th>
              <th className="p-2 text-right">Avg Trade Profit</th>
              <th className="p-2 text-right">Total Trades</th>
            </tr>
          </thead>
          <tbody>
            {performanceData.map((metric, index) => (
              <tr key={index} className="border-b">
                <td className="p-2">{metric.date}</td>
                <td className="p-2 text-right text-green-600">
                  ${metric.totalProfit.toLocaleString()}
                </td>
                <td className="p-2 text-right text-blue-600">
                  {metric.winRate}%
                </td>
                <td className="p-2 text-right text-purple-600">
                  ${metric.avgTradeProfit.toFixed(2)}
                </td>
                <td className="p-2 text-right text-indigo-600">
                  {metric.totalTrades}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default PerformancePage;