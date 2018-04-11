const express = require('express');
const hbs = require('hbs');

// Instantiate new app
var app = express();

app.set('view engine', 'hbs');
app.use(express.static(__dirname + '/public'));

// Register handlers
app.get('/', (req, res) => {
  res.render('home.hbs', {
    pageTitle: 'Home page',
    currYear: new Date().getFullYear(),
    welcomeMsg: 'Welcome to my Node website!'
  });
});

app.get('/about', (req, res) => {
  res.render('about.hbs', {
    pageTitle: 'About page',
    currYear: new Date().getFullYear()
  });
});

app.get('/bad', (req, res) => {
  res.send({
    errorMessage: 'Unable to process request'
  });
});

// Bind app to port on machine
app.listen(3000, () => {
  console.log('Server is up on port 3000');
});
