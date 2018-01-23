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

// Add a new note to file
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
  // Fetch all notes
  var notes = fetchNotes();
  // Filter to only note with matching title
  var matchNote = notes.filter((note) => note.title === title)
  // Return the note or undefined
  return matchNote[0];
};

var removeNote = (title) => {
  // Fetch all notes
  var notes = fetchNotes();
  // Keep notes not matching in title
  var keptNotes = notes.filter((note) => note.title !== title);
  // Write kept notes back to file
  saveNotes(keptNotes);
  // If a note was removed, return true
  return keptNotes.length !== notes.length
};

var logNote = (note) => {
  console.log(`Title: ${note.title}`);
  console.log('------');
  console.log(`Body: ${note.body}`);
};

module.exports = {
  addNote,
  getAll,
  getNote,
  removeNote,
  logNote
}
