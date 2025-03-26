import React from 'react';
import { PieChart, Pie, Cell, ResponsiveContainer, Tooltip } from 'recharts';

const WalletDistributionChart = () => {
  const data = [
    { name: 'BTC', value: 35, color: '#3B82F6' },
    { name: 'ETH', value: 28, color: '#10B981' },
    { name: 'USDT', value: 20, color: '#F59E0B' },
    { name: 'SOL', value: 12, color: '#6366F1' },
    { name: 'Others', value: 5, color: '#EF4444' }
  ];

  return (
    <div className="bg-gray-900 rounded-lg p-4 h-full">
      <h3 className="text-white text-lg mb-4">Wallet Distribution</h3>
      <ResponsiveContainer width="100%" height={250}>
        <PieChart>
          <Pie
            data={data}
            cx="50%"
            cy="50%"
            labelLine={false}
            outerRadius={80}
            fill="#8884d8"
            dataKey="value"
          >
            {data.map((entry, index) => (
              <Cell key={`cell-${index}`} fill={entry.color} />
            ))}
          </Pie>
          <Tooltip 
            contentStyle={{ 
              backgroundColor: '#1f2937', 
              border: 'none',
              borderRadius: '8px'
            }}
            formatter={(value, name) => [`${value}%`, name]}
          />
        </PieChart>
      </ResponsiveContainer>
      <div className="flex justify-center space-x-4 mt-4">
        {data.map((item) => (
          <div key={item.name} className="flex items-center">
            <div 
              className="w-3 h-3 mr-2 rounded-full" 
              style={{ backgroundColor: item.color }}
            />
            <span className="text-white text-sm">{item.name}</span>
          </div>
        ))}
      </div>
    </div>
  );
};

export default WalletDistributionChart;