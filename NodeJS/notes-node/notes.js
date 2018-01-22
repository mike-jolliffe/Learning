// notify that app is running
console.log('Starting notes.js');

// File IO functionality
const fs = require('fs');

// Create an array containing a note object, write to file
var addNote = (title, body) => {
  var notes = [];
  // Note object
  var note = {
    title,
    body
  }

  try {
    var notesString = fs.readFileSync('notes.json');
    notes = JSON.parse(notesString);
  } catch(e){
    // Pass
  }

  var duplicateNotes = notes.filter((note) => note.title === title);

  if (duplicateNotes.length === 0) {
    notes.push(note);
    fs.writeFileSync('notes.json', JSON.stringify(notes));
  }
};

var getAll = () => {
  console.log('Getting all notes')
};

var getNote = (title) => {
  console.log('Getting note', title)
};

var removeNote = (title) => {
  console.log('Removing note', title)
};

module.exports = {
  addNote,
  getAll,
  getNote,
  removeNote
}
