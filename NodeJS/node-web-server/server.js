const express = require('express');

// Instantiate new app
var app = express();

// Register handlers
app.get('/', (req, res) => {
  res.send('<h1>Hello Express!</h1>');
});

app.get('/about', (req, res) => {
  res.send("About page.");
});

app.get('/bad', (req, res) => {
  res.send({
    errorMessage: 'Unable to process request'
  });
});

// Bind app to port on machine
app.listen(3000);
