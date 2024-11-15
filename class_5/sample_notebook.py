class NotebookMain:
    def __init__(self):
        self.note_id = 0
        self.notes_content = {
            1: 'I\'ve done my homework',
            2: 'I ate pizza',
            3: 'I went to GYM'
        }
        
    def show_all_notes(self):
        for key, value in self.notes_content.items():
            if len(value) > 9:
                print(f"{key}: {value[:5]}...{value[-5:]}")
            else:
                print(f"{key}: {value}")
        
        choice = input("Choice: ")
        self.options(choice=choice)
    
    def show_note_details(self):
        id_choice = int(input("Enter note id: "))
        if id_choice in self.notes_content:
            print(
                f"------------------------------------\n"
                f"NOTE {id_choice} DETAILS\n"
                f"Note id: {id_choice}\n"
                f"Note text: {self.notes_content[id_choice]}\n"
            )
        else:
            print("Note not found.")
        choice = input("Choice: ")
        self.options(choice=choice)
    
    def create_note(self):
        new_note = input("Enter text: ")
        self.note_id = max(self.notes_content) + 1
        self.notes_content[self.note_id] = new_note
        print(f"NEW NOTE WITH ID {self.note_id} CREATED")
        choice = input("Choice: ")
        self.options(choice=choice)
    
    def update_note(self):
        id_choice = int(input("Enter note id: "))
        if id_choice in self.notes_content:
            self.notes_content[id_choice] = input("Enter new text: ")
            print(f"NOTE {id_choice} UPDATED")
        else:
            print("Note not found.")
        choice = input("Choice: ")
        self.options(choice=choice)
    
    def delete_note(self):
        id_choice = int(input("Enter note id: "))
        if id_choice in self.notes_content:
            self.notes_content.pop(id_choice)
            print(f"NOTE {id_choice} DELETED")
        else:
            print("Note not found.")
        choice = input("Choice: ")
        self.options(choice=choice)
    
    def options(self, choice):
        if choice == "1":
            self.show_all_notes()
        elif choice == "2":
            self.show_note_details()
        elif choice == "3":
            self.create_note()
        elif choice == "4":
            self.update_note()
        elif choice == "5":
            self.delete_note()
        elif choice == "Q" or choice == "q":
            self.quit()
        elif choice == "M" or choice == "m":
            self.menu()
        else:
            print("Invalid choice.")
            self.menu()
    
    def quit(self):
        print("Exiting the application.")
    
    def menu(self):
        choice = input(
            '''------------------------------------
CHOOSE OPTION
    1: SHOW ALL NOTES
    2: SHOW NOTE DETAILS
    3: CREATE NOTE
    4: UPDATE NOTE
    5: DELETE NOTE
    Q: QUIT THE APPLICATION
    M: SHOW MENU AGAIN
------------------------------------
Choice: '''
        )
        self.options(choice=choice)

nb = NotebookMain()
nb.menu()
