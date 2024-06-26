import { createClient } from "redis";
const util = require("util");
const redis = require("redis");

const redisClient = createClient();
redisClient.on("error", (err) => console.log("Redis client not connected to the server:", err));
redisClient.on("connect", () => console.log("Redis client connected to the server"));

const getAsync = util.promisify(redisClient.get).bind(redisClient);

function setNewSchool(schoolName, value) {
  redisClient.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  const reply = await getAsync(schoolName);
  console.log(reply);
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
