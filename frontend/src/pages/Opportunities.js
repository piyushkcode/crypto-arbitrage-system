import React, { useState } from 'react';
import { arbitrageService } from '../services/arbitrageService';

interface ArbitrageOpportunity {
  id: string;
  sourcePair: string;
  sourceExchange: string;
  destinationPair: string;
  destinationExchange: string;
  potentialProfit: number;
  risk: 'low' | 'medium' | 'high';
}

const OpportunitiesPage: React.FC = () => {
  const [opportunities, setOpportunities] = useState<ArbitrageOpportunity[]>([]);
  const [loading, setLoading] = useState(false);
  const [selectedRisk, setSelectedRisk] = useState<string>('all');

  const fetchOpportunities = async () => {
    setLoading(true);
    try {
      const data = await arbitrageService.getOpportunities();
      setOpportunities(data);
    } catch (error) {
      console.error('Failed to fetch opportunities', error);
    }
    setLoading(false);
  };

  const executeArbitrage = async (opportunityId: string) => {
    try {
      await arbitrageService.executeArbitrage(opportunityId);
      // Refresh opportunities or show success message
      fetchOpportunities();
    } catch (error) {
      console.error('Failed to execute arbitrage', error);
    }
  };

  const filteredOpportunities = selectedRisk === 'all' 
    ? opportunities 
    : opportunities.filter(opp => opp.risk === selectedRisk);

  return (
    <div className="p-4">
      <h1 className="text-2xl mb-4">Arbitrage Opportunities</h1>
      
      <div className="flex justify-between mb-4">
        <div>
          <label className="mr-2">Filter by Risk:</label>
          <select 
            value={selectedRisk}
            onChange={(e) => setSelectedRisk(e.target.value)}
            className="p-2 border rounded"
          >
            <option value="all">All Risks</option>
            <option value="low">Low Risk</option>
            <option value="medium">Medium Risk</option>
            <option value="high">High Risk</option>
          </select>
        </div>
        <button 
          onClick={fetchOpportunities}
          className="bg-blue-500 text-white px-4 py-2 rounded"
          disabled={loading}
        >
          {loading ? 'Fetching...' : 'Refresh Opportunities'}
        </button>
      </div>

      {loading ? (
        <div>Loading opportunities...</div>
      ) : (
        <table className="w-full border-collapse">
          <thead>
            <tr className="bg-gray-100">
              <th className="p-2 border">Source Pair</th>
              <th className="p-2 border">Source Exchange</th>
              <th className="p-2 border">Destination Pair</th>
              <th className="p-2 border">Destination Exchange</th>
              <th className="p-2 border">Potential Profit</th>
              <th className="p-2 border">Risk</th>
              <th className="p-2 border">Actions</th>
            </tr>
          </thead>
          <tbody>
            {filteredOpportunities.map((opp) => (
              <tr key={opp.id} className="hover:bg-gray-50">
                <td className="p-2 border">{opp.sourcePair}</td>
                <td className="p-2 border">{opp.sourceExchange}</td>
                <td className="p-2 border">{opp.destinationPair}</td>
                <td className="p-2 border">{opp.destinationExchange}</td>
                <td className="p-2 border text-green-600">
                  ${opp.potentialProfit.toFixed(2)}
                </td>
                <td className={`p-2 border ${
                  opp.risk === 'low' ? 'text-green-600' : 
                  opp.risk === 'medium' ? 'text-yellow-600' : 'text-red-600'
                }`}>
                  {opp.risk.toUpperCase()}
                </td>
                <td className="p-2 border">
                  <button 
                    onClick={() => executeArbitrage(opp.id)}
                    className="bg-blue-500 text-white px-3 py-1 rounded"
                  >
                    Execute
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default OpportunitiesPage;