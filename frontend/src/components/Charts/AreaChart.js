import React from 'react';
import { AreaChart, Area, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';

interface AreaChartProps {
  data: Array<{
    time: string;
    simpleArbitrage: number;
    triangular: number;
    statistical: number;
  }>;
}

const ArbitragePerformanceChart: React.FC<AreaChartProps> = ({ data }) => {
  return (
    <ResponsiveContainer width="100%" height={300}>
      <AreaChart data={data}>
        <XAxis dataKey="time" />
        <YAxis />
        <Tooltip />
        <Area 
          type="monotone" 
          dataKey="simpleArbitrage" 
          stroke="#8884d8" 
          fill="#8884d8" 
          fillOpacity={0.3} 
        />
        <Area 
          type="monotone" 
          dataKey="triangular" 
          stroke="#82ca9d" 
          fill="#82ca9d" 
          fillOpacity={0.3} 
        />
        <Area 
          type="monotone" 
          dataKey="statistical" 
          stroke="#ffc658" 
          fill="#ffc658" 
          fillOpacity={0.3} 
        />
      </AreaChart>
    </ResponsiveContainer>
  );
};

export default ArbitragePerformanceChart;