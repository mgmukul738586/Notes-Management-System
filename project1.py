notes = []  
def create_note(title, description):
    
    note = {
        "title": title,
        "description": description
    }
    notes.append(note)
    print("Note added successfully.")
def read_notes():
    if not notes:
        print("No notes available.")
        return
    for i, note in enumerate(notes):
        title = note.get("title","(no title)")
        description = note.get("description","(no description)")
        print(f"{i+1}. Title: {title}, Description: {description}")
def update_note(index, new_title, new_description):
    if 0 <= index < len(notes):
        notes[index]['title'] = new_title
        notes[index]['description'] = new_description
        print("Note updated successfully.")
    else:
        print("Invalid note index.")

def delete_note(index):
    if 0 <= index < len(notes):
        removed_note = notes.pop(index)
        print(f"Deleted note: {removed_note['title']}")
    else:
        print("Invalid note index.")
while True:
    print("Notes CRUD Management System")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Update Note")
    print("4. Delete Note")
    print("5. Exit")
    choice = input("Choose an option (1-5): ")
    if choice == "1":
        title = input("Enter note title: ")
        description = input("Enter note description: ")
        create_note(title, description)

    elif choice == "2":
        read_notes()

    elif choice == "3":
        read_notes()
        try:
            idx = int(input("Enter note number to update: ")) - 1
            new_title = input("Enter new title: ")
            new_description = input("Enter new description: ")
            update_note(idx, new_title, new_description)
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "4":
        read_notes()
        try:
            idx = int(input("Enter note number to delete: ")) - 1
            delete_note(idx)
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "5":
        print("Exiting Notes Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
