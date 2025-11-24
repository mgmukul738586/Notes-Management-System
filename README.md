# Notes CRUD Management System

This is a simple command-line Notes CRUD (Create, Read, Update, Delete) Management System implemented in Python.

## Features

- Add new notes with a title and description.
- View all existing notes with their titles and descriptions.
- Update the title and description of an existing note by specifying the note number.
- Delete an existing note by specifying the note number.
- Exit the program safely.

## How to Use

1. Run the Python script.
2. From the menu, select one of the options:
   - `1` to add a new note.
   - `2` to view all notes.
   - `3` to update an existing note (you will be prompted to select which note by number).
   - `4` to delete an existing note (you will be prompted to select which note by number).
   - `5` to exit the program.
3. Follow the on-screen prompts to enter the note details or choose notes to update/delete.

## Code Overview

- The notes data is stored in a list of dictionaries called `notes`.
- Each note is a dictionary with keys `"title"` and `"description"`.
- Functions provided:
  - `create_note(title, description)`: Adds a note to the list.
  - `read_notes()`: Displays all notes.
  - `update_note(index, new_title, new_description)`: Updates a note at the specified list index.
  - `delete_note(index)`: Deletes a note at the specified list index.

## Requirements

- Python 3.x



## License

This project is open source and free to use.

