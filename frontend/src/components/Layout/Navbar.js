import React from 'react';
import { SettingsIcon, SearchIcon, BellIcon } from 'lucide-react';
import { useAuth } from '../../contexts/AuthContext';
import ProfileBadge from '../Common/ProfileBadge';
import SearchBar from '../Common/SearchBar';

const Navbar = () => {
  const { user } = useAuth();

  return (
    <nav className="fixed top-0 right-0 left-64 bg-gray-900 text-white p-4 flex justify-between items-center">
      <SearchBar />
      <div className="flex items-center space-x-4">
        <div className="flex items-center space-x-4">
          <BellIcon className="text-gray-300 hover:text-white cursor-pointer" />
          <SettingsIcon className="text-gray-300 hover:text-white cursor-pointer" />
          <ProfileBadge user={user} />
        </div>
      </div>
    </nav>
  );
};

export default Navbar;