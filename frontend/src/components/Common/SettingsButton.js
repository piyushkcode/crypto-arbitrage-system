import React from 'react';
import { SettingsIcon } from 'lucide-react';

const SettingsButton = () => {
  return (
    <button className="
      bg-gray-800 
      text-gray-300 
      hover:bg-gray-700 
      hover:text-white 
      p-2 
      rounded-full 
      transition-colors
    ">
      <SettingsIcon size={20} />
    </button>
  );
};

export default SettingsButton;