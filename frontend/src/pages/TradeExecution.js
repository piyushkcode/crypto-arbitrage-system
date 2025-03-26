import React, { useState } from 'react';
import { useWebSocket } from '../hooks/useWebSocket';

interface ActiveTrade {
  id: string;
  pair: string;
  exchange: string;
  status: 'pending' | 'executing' | 'completed' | 'failed';
  entryPrice: number;
  exitPrice: number;
  profit: number;
}

const TradeExecutionPage: React.FC = () => {
  const [activeTrades, setActiveTrades] = useState<ActiveTrade[]>([]);
  const { data: liveTradeData, connected } = useWebSocket('wss://api.arbitragepro.com/trades');

  React.useEffect(() => {
    if (liveTradeData) {
      // Update trades based on WebSocket data
      const updateTrades = (currentTrades: ActiveTrade[]) => {
        // Logic to update or add new trades
        if (liveTradeData.type === 'new_trade') {
          return [...currentTrades, liveTradeData.trade];
        }
        return currentTrades.map(trade => 
          trade.id === liveTradeData.tradeId 
            ? { ...trade, ...liveTradeData.updates } 
            : trade
        );
      };

      setActiveTrades(updateTrades);
    }
  }, [liveTradeData]);

  const cancelTrade = (tradeId: string) => {
    // Implement trade cancellation logic
    setActiveTrades(currentTrades => 
      currentTrades.filter(trade => trade.id !== tradeId)
    );
  };

  return (
    <div className="p-4">
      <h1 className="text-2xl mb-4">Trade Execution</h1>
      
      <div className="mb-4">
        <span className="mr-2">WebSocket Status:</span>
        <span className={`
          px-2 py-1 rounded 
          ${connected ? 'bg-green-500 text-white' : 'bg-red-500 text-white'}
        `}>
          {connected ? 'Connected' : 'Disconnected'}
        </span>
      </div>

      <table className="w-full border-collapse">
        <thead>
          <tr className="bg-gray-100">
            <th className="p-2 border">Pair</th>
            <th className="p-2 border">Exchange</th>
            <th className="p-2 border">Status</th>
            <th className="p-2 border">Entry Price</th>
            <th className="p-2 border">Exit Price</th>
            <th className="p-2 border">Profit</th>
            <th className="p-2 border">Actions</th>
          </tr>
        </thead>
        <tbody>
          {activeTrades.map((trade) => (
            <tr key={trade.id} className="hover:bg-gray-50">
              <td className="p-2 border">{trade.pair}</td>
              <td className="p-2 border">{trade.exchange}</td>
              <td className={`p-2 border ${
                trade.status === 'completed' ? 'text-green-600' :
                trade.status === 'failed' ? 'text-red-600' :
                trade.status === 'executing' ? 'text-yellow-600' : ''
              }`}>
                {trade.status.toUpperCase()}
              </td>
              <td className="p-2 border">${trade.entryPrice.toFixed(2)}</td>
              <td className="p-2 border">${trade.exitPrice.toFixed(2)}</td>
              <td className={`p-2 border ${
                trade.profit >= 0 ? 'text-green-600' : 'text-red-600'
              }`}>
                ${trade.profit.toFixed(2)}
              </td>
              <td className="p-2 border">
                <button 
                  onClick={() => cancelTrade(trade.id)}
                  className="bg-red-500 text-white px-3 py-1 rounded"
                  disabled={trade.status !== 'pending'}
                >
                  Cancel
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default TradeExecutionPage;