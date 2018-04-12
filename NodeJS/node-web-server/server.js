const express = require('express');
// Import handlebars
const hbs = require('hbs');
const fs = require('fs');

// Instantiate new app
var app = express();

// Allow partials in template
hbs.registerPartials(__dirname + '/views/partials')
// Make handlebars the engine
app.set('view engine', 'hbs');

// Middleware to log client requests to server
app.use((req, res, next) => {
  // log time, method, and url of user request on site to console
  var now = new Date().toString();
  var log = `${now}: ${req.method} ${req.url}`

  console.log(log);
  fs.appendFile('server.log', log + '\n', (err) => {
    if (err) {
      console.log('Unable to append to server.log.')
    }
  });
  next();
});

// Middleware site maintenance. No next() so won't move on remainder of code.
app.use((req, res, next) => {
  res.render('maintenance.hbs')
});

// Middleware for static
app.use(express.static(__dirname + '/public'));

// Create helper functions for repeated use in templates
hbs.registerHelper('getCurrentYear', () => {
  return new Date().getFullYear()
});

hbs.registerHelper('screamIt', (text) => {
  return text.toUpperCase();
})

// Register handlers
app.get('/', (req, res) => {
  res.render('home.hbs', {
    pageTitle: 'Home page',
    welcomeMsg: 'Welcome to my Node website!'
  });
});

app.get('/about', (req, res) => {
  res.render('about.hbs', {
    pageTitle: 'About page',
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
