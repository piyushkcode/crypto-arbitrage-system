import React from 'react';
import ReactDOM from 'react-dom/client';
import './styles/tailwind.css';
import './styles/theme.css';
import './styles/dashboard.css';
import App from './App';
import { AuthProvider } from './contexts/AuthContext';
import { DashboardProvider } from './contexts/DashboardContext';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <AuthProvider>
      <DashboardProvider>
        <App />
      </DashboardProvider>
    </AuthProvider>
  </React.StrictMode>
);