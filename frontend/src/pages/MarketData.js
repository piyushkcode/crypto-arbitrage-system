import React, { useState } from 'react';
import { useApiData } from '../hooks/useApiData';

interface MarketDataItem {
  symbol: string;
  price: number;
  change24h: number;
  volume: number;
  exchange: string;
}

const MarketDataPage: React.FC = () => {
  const [selectedExchange, setSelectedExchange] = useState<string>('all');
  
  const { data: marketData, loading, error } = useApiData<MarketDataItem[]>(
    `market-data?exchange=${selectedExchange}`, 
    []
  );

  const exchanges = [
    'all', 'Binance', 'Kraken', 'Coinbase', 'KuCoin', 'OKX'
  ];

  if (loading) return <div>Loading market data...</div>;
  if (error) return <div>Error loading market data</div>;

  return (
    <div className="p-4">
      <h1 className="text-2xl mb-4">Market Data</h1>
      
      <div className="mb-4">
        <label className="mr-2">Filter by Exchange:</label>
        <select 
          value={selectedExchange}
          onChange={(e) => setSelectedExchange(e.target.value)}
          className="p-2 border rounded"
        >
          {exchanges.map(exchange => (
            <option key={exchange} value={exchange}>
              {exchange}
            </option>
          ))}
        </select>
      </div>

      <table className="w-full border-collapse">
        <thead>
          <tr className="bg-gray-100">
            <th className="p-2 border">Symbol</th>
            <th className="p-2 border">Price</th>
            <th className="p-2 border">24h Change</th>
            <th className="p-2 border">Volume</th>
            <th className="p-2 border">Exchange</th>
          </tr>
        </thead>
        <tbody>
          {marketData.map((item, index) => (
            <tr key={index} className="hover:bg-gray-50">
              <td className="p-2 border">{item.symbol}</td>
              <td className="p-2 border">${item.price.toFixed(2)}</td>
              <td className={`p-2 border ${
                item.change24h >= 0 ? 'text-green-600' : 'text-red-600'
              }`}>
                {item.change24h.toFixed(2)}%
              </td>
              <td className="p-2 border">${item.volume.toLocaleString()}</td>
              <td className="p-2 border">{item.exchange}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default MarketDataPage;