import React from 'react';
import { PieChart, Pie, Cell, ResponsiveContainer, Tooltip } from 'recharts';

interface WalletDistributionData {
  name: string;
  value: number;
  color: string;
}

const WalletDistributionChart: React.FC = () => {
  const data: WalletDistributionData[] = [
    { name: 'BTC', value: 35, color: '#0088FE' },
    { name: 'ETH', value: 28, color: '#00C49F' },
    { name: 'USDT', value: 20, color: '#FFBB28' },
    { name: 'SOL', value: 12, color: '#FF8042' },
    { name: 'Others', value: 5, color: '#8884D8' }
  ];

  return (
    <ResponsiveContainer width="100%" height={300}>
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
        <Tooltip />
      </PieChart>
    </ResponsiveContainer>
  );
};

export default WalletDistributionChart;