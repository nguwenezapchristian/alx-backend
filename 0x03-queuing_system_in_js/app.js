const express = require('express');
const redis = require('redis');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

app.use(bodyParser.json());

// Create Redis clients for publisher and subscriber
const publisher = redis.createClient();
const subscriber = redis.createClient();

publisher.on('error', (err) => {
  console.error('Publisher Redis error:', err);
});

subscriber.on('error', (err) => {
  console.error('Subscriber Redis error:', err);
});

// Endpoint to publish a message
app.post('/publish', (req, res) => {
  const { channel, message } = req.body;
  publisher.publish(channel, message, (err, reply) => {
    if (err) {
      res.status(500).send('Error publishing message');
    } else {
      res.send(`Message published to channel ${channel}`);
    }
  });
});

// Subscribe to a channel and log messages
app.get('/subscribe/:channel', (req, res) => {
  const channel = req.params.channel;

  subscriber.subscribe(channel, (err, reply) => {
    if (err) {
      res.status(500).send('Error subscribing to channel');
    } else {
      res.send(`Subscribed to channel ${channel}`);
    }
  });
});

subscriber.on('message', (channel, message) => {
  console.log(`Received message from ${channel}: ${message}`);
});

// Start the server
app.listen(port, () => {
  console.log(`Express app listening at http://localhost:${port}`);
});
