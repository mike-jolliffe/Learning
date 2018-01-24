const fs = require('fs');
const _ = require('lodash');
const yargs = require('yargs');

const notes = require('./notes.js');

const argv = yargs.argv;
var command = argv._[0];

if (command === 'add') {
  var note = notes.addNote(argv.title, argv.body);
  if (note) {
    notes.logNote(note);
  } else {
    console.log('There was a problem creating the note!!');
  }
} else if (command === 'list') {
  var allNotes = notes.getAll();
  console.log(`Getting ${allNotes.length} note(s).`);
  allNotes.forEach((note) => notes.logNote(note));
} else if (command === 'read') {
  var note = notes.getNote(argv.title);
  if (note) {
    notes.logNote(note);
  } else {
    console.log(`Note with title ${argv.title} not found`);
  }
} else if (command === 'remove') {
  var removed = notes.removeNote(argv.title);
  var message = removed ? `Removed note titled ${argv.title}.` :
                          `Unable to remove note titled ${argv.title}.`;
  console.log(message);
} else {
  console.log('command not recognized')
}
