import React, { useState } from 'react';
import { walletService } from '../services/walletService';

interface Wallet {
  currency: string;
  balance: number;
  address: string;
}

const WalletManagerPage: React.FC = () => {
  const [wallets, setWallets] = useState<Wallet[]>([]);
  const [selectedCurrency, setSelectedCurrency] = useState('');
  const [transferAmount, setTransferAmount] = useState('');
  const [destinationAddress, setDestinationAddress] = useState('');

  const fetchWallets = async () => {
    try {
      const walletData = await walletService.getWalletBalance();
      setWallets(walletData);
    } catch (error) {
      console.error('Failed to fetch wallets', error);
    }
  };

  const transferFunds = async () => {
    if (!selectedCurrency || !transferAmount || !destinationAddress) {
      alert('Please fill all fields');
      return;
    }

    try {
      await walletService.transferFunds({
        from: selectedCurrency,
        to: destinationAddress,
        amount: parseFloat(transferAmount),
        currency: selectedCurrency
      });
      
      // Refresh wallets after transfer
      fetchWallets();
      
      // Reset form
      setSelectedCurrency('');
      setTransferAmount('');
      setDestinationAddress('');
    } catch (error) {
      console.error('Transfer failed', error);
    }
  };

  React.useEffect(() => {
    fetchWallets();
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-2xl mb-4">Wallet Manager</h1>
      
      <div className="grid grid-cols-2 gap-4">
        {/* Wallet Balances */}
        <div className="bg-gray-100 p-4 rounded">
          <h2 className="text-xl mb-4">Wallet Balances</h2>
          <table className="w-full">
            <thead>
              <tr>
                <th className="text-left">Currency</th>
                <th className="text-right">Balance</th>
              </tr>
            </thead>
            <tbody>
              {wallets.map((wallet, index) => (
                <tr key={index}>
                  <td>{wallet.currency}</td>
                  <td className="text-right">
                    {wallet.balance.toFixed(4)} {wallet.currency}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        {/* Transfer Funds */}
        <div className="bg-gray-100 p-4 rounded">
          <h2 className="text-xl mb-4">Transfer Funds</h2>
          <div className="space-y-4">
            <select 
              value={selectedCurrency}
              onChange={(e) => setSelectedCurrency(e.target.value)}
              className="w-full p-2 border rounded"
            >
              <option value="">Select Currency</option>
              {wallets.map((wallet, index) => (
                <option key={index} value={wallet.currency}>
                  {wallet.currency}
                </option>
              ))}
            </select>

            <input 
              type="number"
              placeholder="Amount"
              value={transferAmount}
              onChange={(e) => setTransferAmount(e.target.value)}
              className="w-full p-2 border rounded"
            />

            <input 
              type="text"
              placeholder="Destination Address"
              value={destinationAddress}
              onChange={(e) => setDestinationAddress(e.target.value)}
              className="w-full p-2 border rounded"
            />

            <button 
              onClick={transferFunds}
              className="w-full bg-blue-500 text-white p-2 rounded"
            >
              Transfer Funds
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default WalletManagerPage;