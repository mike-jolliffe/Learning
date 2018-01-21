console.log('Starting app...');

const fs = require('fs');
const os = require('os');

var user = os.userInfo();

//Create a new text file and append Hello World to it
fs.appendFile('greetings.txt', `Hello ${user.username}!`, function(err) {
  if (err) {
    console.log('Unable to write to file.');
  }
});
