import { createClient } from "redis";

const redisClient = createClient();
redisClient.on("error", (err) => console.log("Redis client not connected to the server:", err));
redisClient.on("connect", () => console.log("Redis client connected to the server"));