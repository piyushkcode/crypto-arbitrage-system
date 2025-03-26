import React from 'react';
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';

interface AIMarketPredictionsData {
  time: string;
  prediction: number;
}

const AIMarketPredictionsChart: React.FC = () => {
  const data: AIMarketPredictionsData[] = [
    { time: '00:00', prediction: 0 },
    { time: '03:00', prediction: 0.5 },
    { time: '06:00', prediction: 1 },
    { time: '09:00', prediction: 1.5 },
    { time: '12:00', prediction: 2 },
    { time: '15:00', prediction: 2.5 },
    { time: '18:00', prediction: 3 },
    { time: '21:00', prediction: 3.5 }
  ];

  return (
    <ResponsiveContainer width="100%" height={300}>
      <LineChart data={data}>
        <XAxis dataKey="time" />
        <YAxis />
        <Tooltip />
        <Line 
          type="monotone" 
          dataKey="prediction" 
          stroke="#8884d8" 
          strokeWidth={2} 
        />
      </LineChart>
    </ResponsiveContainer>
  );
};

export default AIMarketPredictionsChart;