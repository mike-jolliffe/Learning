// Require file IO functionality
const fs = require('fs');

// Create a JS object
var origNote = {
  title: 'First Note',
  body: 'Here is the body of the first note.'
}

// Serialize JS object to JSON string and write to file
var jsonString = JSON.stringify(origNote);
fs.writeFileSync('origNote.json', jsonString);

// Read JSON file and deserialize string back to JS object
var noteString = fs.readFileSync('origNote.json');
var note = JSON.parse(noteString);

// Check that deserialization worked
console.log(typeof note);
console.log(note.title);
