import React from 'react';
import { ChevronDownIcon } from 'lucide-react';

const ProfileBadge = ({ user }) => {
  return (
    <div className="flex items-center cursor-pointer">
      <div className="mr-3">
        <div className="text-white font-semibold">{user?.name || 'Alex Morgan'}</div>
        <div className="text-xs text-green-500">PRO</div>
      </div>
      <div className="w-10 h-10 bg-gray-700 rounded-full flex items-center justify-center">
        <span className="text-white font-bold">
          {user?.initials || 'AM'}
        </span>
      </div>
      <ChevronDownIcon className="ml-2 text-gray-400" size={16} />
    </div>
  );
};

export default ProfileBadge;