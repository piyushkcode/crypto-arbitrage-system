import React, { createContext, useState, useContext } from 'react';

interface User {
  id: string;
  name: string;
  email: string;
  role: 'user' | 'pro' | 'admin';
}

interface AuthContextType {
  user: User | null;
  login: (email: string, password: string) => Promise<void>;
  logout: () => void;
  isAuthenticated: boolean;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);

  const login = async (email: string, password: string) => {
    // Implement actual login logic
    try {
      // Placeholder for API call
      const userData: User = {
        id: '1',
        name: 'Alex Morgan',
        email: email,
        role: 'pro'
      };
      setUser(userData);
    } catch (error) {
      throw new Error('Login failed');
    }
  };

  const logout = () => {
    setUser(null);
  };

  const authContext: AuthContextType = {
    user,
    login,
    logout,
    isAuthenticated: !!user
  };

  return (
    <AuthContext.Provider value={authContext}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};