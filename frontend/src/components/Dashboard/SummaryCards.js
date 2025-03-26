import React from 'react';
import { TrendingUpIcon, ChartIcon, CheckCircleIcon, WalletIcon } from 'lucide-react';

const SummaryCards = () => {
  const summaryData = [
    {
      title: 'Total Profit (24h)',
      value: '+$18,724.53',
      change: '+5.8%',
      icon: TrendingUpIcon,
      color: 'text-green-500'
    },
    {
      title: 'Current Opportunities',
      value: '37',
      change: '12 new since last hour',
      icon: ChartIcon,
      color: 'text-blue-500'
    },
    {
      title: 'Win Rate',
      value: '94.3%',
      change: '+2.1% improvement',
      icon: CheckCircleIcon,
      color: 'text-purple-500'
    },
    {
      title: 'Total Balance',
      value: '$527,392.15',
      change: '+$32,541 (24h)',
      icon: WalletIcon,
      color: 'text-yellow-500'
    }
  ];

  return (
    <div className="grid grid-cols-4 gap-4">
      {summaryData.map((card, index) => (
        <div 
          key={index} 
          className="bg-gray-900 rounded-lg p-4 flex items-center justify-between"
        >
          <div>
            <div className="text-gray-400 text-sm mb-2">{card.title}</div>
            <div className="text-white text-xl font-bold">{card.value}</div>
            <div className={`text-xs ${card.color}`}>{card.change}</div>
          </div>
          <card.icon className={`${card.color} opacity-70`} size={32} />
        </div>
      ))}
    </div>
  );
};

export default SummaryCards;