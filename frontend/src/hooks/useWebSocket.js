import { useState, useEffect, useCallback } from 'react';

interface WebSocketHook {
  data: any;
  sendMessage: (message: any) => void;
  connected: boolean;
}

export const useWebSocket = (url: string): WebSocketHook => {
  const [socket, setSocket] = useState<WebSocket | null>(null);
  const [data, setData] = useState<any>(null);
  const [connected, setConnected] = useState(false);

  useEffect(() => {
    const ws = new WebSocket(url);

    ws.onopen = () => {
      setSocket(ws);
      setConnected(true);
    };

    ws.onmessage = (event) => {
      try {
        const parsedData = JSON.parse(event.data);
        setData(parsedData);
      } catch (error) {
        console.error('Error parsing WebSocket message', error);
      }
    };

    ws.onclose = () => {
      setConnected(false);
    };

    return () => {
      ws.close();
    };
  }, [url]);

  const sendMessage = useCallback((message: any) => {
    if (socket && socket.readyState === WebSocket.OPEN) {
      socket.send(JSON.stringify(message));
    }
  }, [socket]);

  return { data, sendMessage, connected };
};