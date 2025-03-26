import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { 
  HomeIcon, 
  TrendingUpIcon, 
  BarChartIcon, 
  WalletIcon, 
  SettingsIcon, 
  ActivityIcon 
} from 'lucide-react';

const menuItems = [
  { 
    name: 'Dashboard', 
    icon: HomeIcon, 
    path: '/dashboard' 
  },
  { 
    name: 'Market Data', 
    icon: TrendingUpIcon, 
    path: '/market-data' 
  },
  { 
    name: 'Opportunities', 
    icon: BarChartIcon, 
    path: '/opportunities' 
  },
  { 
    name: 'Trade Execution', 
    icon: ActivityIcon, 
    path: '/trade-execution' 
  },
  { 
    name: 'AI Center', 
    icon: SettingsIcon, 
    path: '/ai-center' 
  },
  { 
    name: 'Wallet Manager', 
    icon: WalletIcon, 
    path: '/wallet' 
  }
];

const Sidebar = () => {
  const location = useLocation();

  return (
    <div className="fixed left-0 top-0 h-full w-64 bg-gray-900 text-white p-4">
      <div className="flex items-center mb-8">
        <div className="text-2xl font-bold text-green-500">ARBITRAGE PRO</div>
      </div>
      <nav>
        {menuItems.map((item) => (
          <Link 
            key={item.path} 
            to={item.path} 
            className={`
              flex items-center p-3 mb-2 rounded-lg transition-colors 
              ${location.pathname === item.path 
                ? 'bg-green-500 text-white' 
                : 'hover:bg-gray-800 text-gray-300'
              }
            `}
          >
            <item.icon className="mr-3" size={20} />
            {item.name}
          </Link>
        ))}
      </nav>
    </div>
  );
};

export default Sidebar;