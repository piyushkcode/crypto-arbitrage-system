import React from 'react';
import Sidebar from './Sidebar';
import Navbar from './Navbar';

const MainLayout = ({ children }) => {
  return (
    <div className="flex h-screen bg-gray-800 text-white">
      <Sidebar />
      <div className="flex-1 ml-64 mt-16 overflow-y-auto">
        <Navbar />
        <main className="p-6 pt-24">
          {children}
        </main>
      </div>
    </div>
  );
};

export default MainLayout;