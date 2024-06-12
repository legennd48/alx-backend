import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error('Redis client not connected to the server:', err.message);
});

function setHashFields() {
  const hashKey = 'HolbertonSchools';
  const schools = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  };
  for (const [field, value] of Object.entries(schools)) {
    client.hset(hashKey, field, value, redis.print);
  }
}

function displayHash() {
  const hashKey = 'HolbertonSchools';
  client.hgetall(hashKey, (_err, obj) => {
    console.log('HolbertonSchools:', obj);
  });
}

// Set the hash fields
setHashFields();

// Display the hash fields
displayHash();

export default client;
