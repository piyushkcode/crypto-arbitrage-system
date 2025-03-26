import React, { useState } from 'react';
import { SearchIcon } from 'lucide-react';

const SearchBar = () => {
  const [searchTerm, setSearchTerm] = useState('');

  return (
    <div className="relative flex items-center">
      <SearchIcon 
        className="absolute left-3 text-gray-400" 
        size={20} 
      />
      <input 
        type="text" 
        placeholder="Search..." 
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
        className="
          pl-10 pr-4 py-2 
          bg-gray-800 
          text-white 
          rounded-lg 
          w-64 
          focus:outline-none 
          focus:ring-2 
          focus:ring-green-500
        "
      />
    </div>
  );
};

export default SearchBar;