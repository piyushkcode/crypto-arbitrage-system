import React, { useState, useEffect } from 'react';

interface AIModel {
  id: string;
  name: string;
  accuracy: number;
  performanceMetrics: {
    precision: number;
    recall: number;
    f1Score: number;
  };
  status: 'active' | 'training' | 'idle';
}

interface AIStrategy {
  id: string;
  name: string;
  description: string;
  modelId: string;
  profitability: number;
  risk: 'low' | 'medium' | 'high';
}

const AICenterPage: React.FC = () => {
  const [aiModels, setAIModels] = useState<AIModel[]>([]);
  const [aiStrategies, setAIStrategies] = useState<AIStrategy[]>([]);
  const [selectedModel, setSelectedModel] = useState<string | null>(null);

  const fetchAIData = async () => {
    try {
      // Simulate API call
      const mockModels: AIModel[] = [
        {
          id: 'model1',
          name: 'Arbitrage Predictor v3',
          accuracy: 94.5,
          performanceMetrics: {
            precision: 0.92,
            recall: 0.96,
            f1Score: 0.94
          },
          status: 'active'
        },
        {
          id: 'model2',
          name: 'Market Trend Analyzer',
          accuracy: 89.3,
          performanceMetrics: {
            precision: 0.87,
            recall: 0.91,
            f1Score: 0.89
          },
          status: 'training'
        }
      ];

      const mockStrategies: AIStrategy[] = [
        {
          id: 'strategy1',
          name: 'Cross-Exchange Arbitrage',
          description: 'Identifies price discrepancies across multiple exchanges',
          modelId: 'model1',
          profitability: 12.5,
          risk: 'low'
        },
        {
          id: 'strategy2',
          name: 'Triangular Arbitrage',
          description: 'Exploits price differences in triangular trading',
          modelId: 'model2',
          profitability: 8.7,
          risk: 'medium'
        }
      ];

      setAIModels(mockModels);
      setAIStrategies(mockStrategies);
    } catch (error) {
      console.error('Failed to fetch AI data', error);
    }
  };

  useEffect(() => {
    fetchAIData();
  }, []);

  const handleModelSelect = (modelId: string) => {
    setSelectedModel(modelId === selectedModel ? null : modelId);
  };

  return (
    <div className="p-4 space-y-6">
      <h1 className="text-2xl font-bold mb-4">AI Center</h1>

      <div className="grid grid-cols-2 gap-6">
        {/* AI Models Section */}
        <div className="bg-gray-100 p-4 rounded-lg">
          <h2 className="text-xl font-semibold mb-4">AI Models</h2>
          {aiModels.map((model) => (
            <div 
              key={model.id}
              className={`p-3 mb-2 rounded cursor-pointer ${
                selectedModel === model.id 
                  ? 'bg-blue-200' 
                  : 'bg-white hover:bg-gray-200'
              }`}
              onClick={() => handleModelSelect(model.id)}
            >
              <div className="flex justify-between items-center">
                <span className="font-medium">{model.name}</span>
                <span className={`
                  px-2 py-1 rounded text-sm
                  ${model.status === 'active' ? 'bg-green-500 text-white' : 
                    model.status === 'training' ? 'bg-yellow-500 text-white' : 
                    'bg-gray-500 text-white'}
                `}>
                  {model.status.toUpperCase()}
                </span>
              </div>
              {selectedModel === model.id && (
                <div className="mt-2 space-y-2">
                  <p>Accuracy: {model.accuracy}%</p>
                  <div className="bg-white p-2 rounded">
                    <h3 className="font-semibold">Performance Metrics</h3>
                    <p>Precision: {model.performanceMetrics.precision}</p>
                    <p>Recall: {model.performanceMetrics.recall}</p>
                    <p>F1 Score: {model.performanceMetrics.f1Score}</p>
                  </div>
                </div>
              )}
            </div>
          ))}
        </div>

        {/* AI Strategies Section */}
        <div className="bg-gray-100 p-4 rounded-lg">
          <h2 className="text-xl font-semibold mb-4">AI Strategies</h2>
          {aiStrategies.map((strategy) => (
            <div 
              key={strategy.id} 
              className="bg-white p-3 mb-2 rounded"
            >
              <div className="flex justify-between items-center">
                <h3 className="font-medium">{strategy.name}</h3>
                <span className={`
                  px-2 py-1 rounded text-sm
                  ${strategy.risk === 'low' ? 'bg-green-500 text-white' : 
                    strategy.risk === 'medium' ? 'bg-yellow-500 text-white' : 
                    'bg-red-500 text-white'}
                `}>
                  {strategy.risk.toUpperCase()} RISK
                </span>
              </div>
              <p className="text-gray-600 mt-2">{strategy.description}</p>
              <div className="mt-2 flex justify-between">
                <span>Associated Model: {strategy.modelId}</span>
                <span className="font-semibold text-green-600">
                  Profitability: {strategy.profitability}%
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default AICenterPage;