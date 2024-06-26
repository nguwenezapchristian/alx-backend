import { createClient } from "redis";

const redis = require("redis");
const redisClient = createClient();
redisClient.on("error", (err) => console.log("Redis client not connected to the server:", err));
redisClient.on("connect", () => console.log("Redis client connected to the server"));

function setNewSchool(schoolName, value) {
  redisClient.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
  redisClient.get(schoolName, (err, reply) => {
    console.log(reply);
  });
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
setNewSchool('LDK', 100);
displaySchoolValue('LDK');
