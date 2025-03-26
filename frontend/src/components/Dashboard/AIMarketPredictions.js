import React from 'react';
import { AreaChart, Area, XAxis, Tooltip, ResponsiveContainer } from 'recharts';

const AIMarketPredictions = () => {
  const predictionData = [
    { time: '00:00', prediction: 0 },
    { time: '03:00', prediction: 0.5 },
    { time: '06:00', prediction: 1.2 },
    { time: '09:00', prediction: 1.8 },
    { time: '12:00', prediction: 2.3 },
    { time: '15:00', prediction: 2.7 },
    { time: '18:00', prediction: 2.9 },
    { time: '21:00', prediction: 3.1 }
  ];

  return (
    <div className="bg-gray-900 rounded-lg p-4 h-full">
      <h3 className="text-white text-lg mb-4">AI Market Predictions</h3>
      <ResponsiveContainer width="100%" height={250}>
        <AreaChart data={predictionData}>
          <defs>
            <linearGradient id="colorPrediction" x1="0" y1="0" x2="0" y2="1">
              <stop offset="5%" stopColor="#8b5cf6" stopOpacity={0.8}/>
              <stop offset="95%" stopColor="#8b5cf6" stopOpacity={0}/>
            </linearGradient>
          </defs>
          <XAxis 
            dataKey="time" 
            axisLine={false} 
            tickLine={false} 
            stroke="#666" 
          />
          <Tooltip 
            contentStyle={{ 
              backgroundColor: '#1f2937', 
              border: 'none',
              borderRadius: '8px'
            }}
          />
          <Area 
            type="monotone" 
            dataKey="prediction" 
            stroke="#8b5cf6" 
            fillOpacity={1} 
            fill="url(#colorPrediction)"
          />
        </AreaChart>
      </ResponsiveContainer>
    </div>
  );
};

export default AIMarketPredictions;