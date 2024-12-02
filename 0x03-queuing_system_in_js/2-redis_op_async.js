import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

function setNewSchool (schoolName, value) {
  client.set(schoolName, value, redis.print);
}

const getAsync = promisify(client.get).bind(client);

async function displaySchoolValue (schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.error(err);
  }
}

async function main() {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}

client.on('connect', async () => {
  console.log(`Redis client connected to the server`);
  await main();
});
