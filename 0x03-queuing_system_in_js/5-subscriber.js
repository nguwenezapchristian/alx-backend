import { createClient } from "redis";

const redisClient = createClient();

redisClient.on("error", (err) => console.log("Redis client not connected to the server:", err));
redisClient.on("connect", () => console.log("Redis client connected to the server"));
redisClient.subscribe("holberton school channel");

redisClient.on("message", (channel, message) => {
  if (message === "KILL_SERVER") {
    redisClient.unsubscribe();
    redisClient.quit();
  }
  console.log(message);
});