import redis from 'redis';

const client = redis.createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

client.on('connect', async () => {
  console.log('Redis client connected to the server');

  // Create Hash
  const hashKey = 'HolbertonSchools';
  const hashObj = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2
  };

  for (const [city, value] of Object.entries(hashObj)) {
    client.hset(hashKey, city, value, redis.print);
  }

  // Display Hash
  client.hgetall(hashKey, (err, result) => {
    if (err) {
      console.error(err);
    } else {
      console.log(result);
    }

    client.quit();
  });
});
