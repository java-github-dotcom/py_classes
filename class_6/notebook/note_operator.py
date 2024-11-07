from tabulate import tabulate
import os
import pandas as pd

class BaseMethods:
    def __init__(self):
        # Define the path to note_archive.csv relative to the script's location
        self.file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'note_archive.csv')
        
        self.choice = {
            '1': 'Show all notes',
            '2': 'Show note details',
            '3': 'Create note',
            '4': 'Update note',
            '5': 'Delete note',
            'Q': 'Quit the application',
            'M': 'Show menu again'
        }
        
        # Attempt to read the file or create it if it doesn't exist
        try:
            self.note_data = pd.read_csv(self.file_path)
        except FileNotFoundError:
            # If the file doesn't exist, create it with header
            with open(self.file_path, 'w') as f:
                f.write('id,text\n')  # Set up CSV headers
            self.note_data = pd.read_csv(self.file_path)

class BaseOperations(BaseMethods):
    def __init__(self):
        super().__init__()

    def truncate_text(self, text, length=6):
        """Truncate text to show only the first and last `length` characters."""
        if len(text) > 2 * length:
            return f"{text[:length]}...{text[-length:]}"
        return text

    def show_all_notes(self):
        if not self.note_data.empty:
            # Apply text truncation only in show_all_notes
            display_data = self.note_data.copy()
            display_data['text'] = display_data['text'].apply(self.truncate_text)
            return tabulate(display_data, headers='keys', tablefmt='rounded_grid', showindex=False)
        return "No notes found."

    def show_note_details(self, note_id):
        # Show the full text for a specific note
        note = self.note_data[self.note_data['id'] == note_id]
        if not note.empty:
            return tabulate(note, headers='keys', tablefmt='rounded_grid', showindex=False)
        return 'Note ID not found.'

    def create_note(self, text):
        new_id = self.note_data['id'].max() + 1 if not self.note_data.empty else 1
        new_note = pd.DataFrame([[new_id, text]], columns=['id', 'text'])
        self.note_data = pd.concat([self.note_data, new_note], ignore_index=True)
        self.note_data.to_csv('note_archive.csv', index=False)
        return "Note created successfully."

    def update_note(self, note_id, new_text):
        if note_id in self.note_data['id'].values:
            self.note_data.loc[self.note_data['id'] == note_id, 'text'] = new_text
            self.note_data.to_csv('note_archive.csv', index=False)
            return "Note updated successfully."
        return "Note ID not found."

    def delete_note(self, note_id):
        if note_id in self.note_data['id'].values:
            self.note_data = self.note_data[self.note_data['id'] != note_id]
            self.note_data.to_csv('note_archive.csv', index=False)
            return "Note deleted successfully."
        return "Note ID not found."

    def get_menu(self):
        return "\n".join([f"{k}: {v}" for k, v in self.choice.items()])

class UI:
    def __init__(self):
        self.operations = BaseOperations()

    def display_menu(self):
        print("\nMenu:")
        print(self.operations.get_menu())

    def get_choice(self):
        return input("\nEnter your choice: ").strip().upper()

    def start(self):
        self.display_menu()
        while True:
            choice = self.get_choice()
            if choice == '1':
                print(self.operations.show_all_notes())
            elif choice == '2':
                try:
                    note_id = int(input("Enter note ID to view details: "))
                    print(self.operations.show_note_details(note_id))
                except ValueError:
                    print("Invalid ID. Please enter a number.")
            elif choice == '3':
                note_text = input("Enter note text: ")
                print(self.operations.create_note(note_text))
            elif choice == '4':
                try:
                    note_id = int(input("Enter note ID to update: "))
                    new_text = input("Enter new note text: ")
                    print(self.operations.update_note(note_id, new_text))
                except ValueError:
                    print("Invalid ID. Please enter a number.")
            elif choice == '5':
                try:
                    note_id = int(input("Enter note ID to delete: "))
                    print(self.operations.delete_note(note_id))
                except ValueError:
                    print("Invalid ID. Please enter a number.")
            elif choice == 'Q':
                print("Quitting the application.")
                break
            elif choice == 'M':
                self.display_menu()
            else:
                print("Invalid choice, please select again.")

# Initialize and start the UI
app = UI()
app.start()
