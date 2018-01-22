// notify that app is running
console.log('Starting notes.js');

// File IO functionality
const fs = require('fs');

// Fetch all notes from file
var fetchNotes = () => {
  try {
    var notesString = fs.readFileSync('notes.json');
    return JSON.parse(notesString);
  } catch(e){
    return [];
  }
};

// Save all notes to file
var saveNotes = (notes) => {
  fs.writeFileSync('notes.json', JSON.stringify(notes));
}

// Create an array containing a note object, write to file
var addNote = (title, body) => {
  var notes = fetchNotes();
  // Note object
  var note = {
    title,
    body
  }

  var duplicateNotes = notes.filter((note) => note.title === title);

  if (duplicateNotes.length === 0) {
    notes.push(note);
    saveNotes(notes);
    return note;
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
