import { useState, useEffect } from 'react';
import axios from 'axios';

export const useApiData = <T>(endpoint: string, initialData: T) => {
  const [data, setData] = useState<T>(initialData);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const response = await axios.get(`/api/${endpoint}`);
        setData(response.data);
        setLoading(false);
      } catch (err) {
        setError('Failed to fetch data');
        setLoading(false);
      }
    };

    fetchData();
  }, [endpoint]);

  return { data, loading, error };
};