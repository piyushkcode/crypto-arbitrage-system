import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { useAuth } from './contexts/AuthContext';

// Import Pages
import Dashboard from './pages/Dashboard';
import Login from './pages/Login';
import Signup from './pages/Signup';
import MarketData from './pages/MarketData';
import Opportunities from './pages/Opportunities';
import TradeExecution from './pages/TradeExecution';
import AiCenter from './pages/AiCenter';
import WalletManager from './pages/WalletManager';
import PerformancePage from './pages/PerformancePage';

// Import Layout Components
import MainLayout from './components/Layout/MainLayout';

function PrivateRoute({ children }) {
  const { isAuthenticated } = useAuth();
  return isAuthenticated ? (
    <MainLayout>{children}</MainLayout>
  ) : (
    <Navigate to="/login" replace />
  );
}

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        
        <Route 
          path="/dashboard" 
          element={
            <PrivateRoute>
              <Dashboard />
            </PrivateRoute>
          } 
        />
        <Route 
          path="/market-data" 
          element={
            <PrivateRoute>
              <MarketData />
            </PrivateRoute>
          } 
        />
        <Route 
          path="/opportunities" 
          element={
            <PrivateRoute>
              <Opportunities />
            </PrivateRoute>
          } 
        />
        <Route 
          path="/trade-execution" 
          element={
            <PrivateRoute>
              <TradeExecution />
            </PrivateRoute>
          } 
        />
        <Route 
          path="/ai-center" 
          element={
            <PrivateRoute>
              <AiCenter />
            </PrivateRoute>
          } 
        />
        <Route 
          path="/wallet" 
          element={
            <PrivateRoute>
              <WalletManager />
            </PrivateRoute>
          } 
        />
        <Route 
          path="/performance" 
          element={
            <PrivateRoute>
              <PerformancePage />
            </PrivateRoute>
          } 
        />
        
        {/* Redirect to dashboard by default for authenticated users */}
        <Route 
          path="/" 
          element={<Navigate to="/dashboard" replace />} 
        />
      </Routes>
    </Router>
  );
}

export default App;