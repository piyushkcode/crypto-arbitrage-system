import React from 'react';
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';

const PerformanceChart = ({ data }) => {
  return (
    <div className="bg-gray-900 rounded-lg p-4">
      <h3 className="text-white text-lg mb-4">Arbitrage Performance</h3>
      <div className="flex space-x-2 mb-4">
        {['Simple', 'Triangular', 'Statistical'].map((type, index) => (
          <button 
            key={type} 
            className={`
              px-3 py-1 rounded-lg text-sm 
              ${index === 0 ? 'bg-blue-500 text-white' : 'bg-gray-700 text-gray-400'}
            `}
          >
            {type} Arbitrage
          </button>
        ))}
        <div className="ml-auto flex space-x-2">
          {['1D', '1W', '1M'].map((period) => (
            <button 
              key={period} 
              className="bg-gray-700 text-gray-400 px-3 py-1 rounded-lg text-sm"
            >
              {period}
            </button>
          ))}
        </div>
      </div>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={data}>
          <XAxis dataKey="time" stroke="#888" />
          <YAxis stroke="#888" />
          <Tooltip 
            contentStyle={{ backgroundColor: '#1f2937', border: 'none' }}
            itemStyle={{ color: '#white' }}
          />
          <Line type="monotone" dataKey="simple" stroke="#3b82f6" strokeWidth={2} />
          <Line type="monotone" dataKey="triangular" stroke="#8b5cf6" strokeWidth={2} />
          <Line type="monotone" dataKey="statistical" stroke="#10b981" strokeWidth={2} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
};

export default PerformanceChart;