import redis from 'redis';

// Create a Redis client instance
const client = redis.createClient();

// Event listener for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event listener for errors
client.on('error', (err) => {
  console.error('Redis client not connected to the server:', err.message);
});

// Subscribe to the 'holberton school channel'
client.subscribe('holberton school channel');

// Listen for messages on the 'holberton school channel'
client.on('message', (channel, message) => {
  if (message === 'KILL_SERVER') {
    client.unsubscribe(channel);
    client.quit();
  }
  console.log(message);
});

export default client;
