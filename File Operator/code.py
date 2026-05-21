import os
from datetime import datetime

class JournalManager:
    def __init__(self):
        self.filename = "journal.txt"

    def add_entry(self):
        """Appends a new entry with a timestamp to the file."""
        user_text = input("\nEnter your journal entry: ")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            
            with open(self.filename, "a") as file:
                file.write(f"[{timestamp}]\n{user_text}\n\n")
            print("Entry added successfully!")
        except PermissionError:
            print("Error: You do not have permission to write to this file.")

    def view_all_entries(self):
        """Reads and displays all entries from the journal file."""
        try:
            with open(self.filename, "r") as file:
                content = file.read()
                if not content:
                    print("\nYour journal is empty.")
                else:
                    print("\n--- Your Journal Entries ---")
                    print(content)
        except FileNotFoundError:
            print("\nError: The journal file does not exist. Please add a new entry first.")

    def search_entry(self):
        """Searches for a specific keyword or date within the file."""
        if not os.path.exists(self.filename):
            print("\nError: No journal found to search.")
            return

        keyword = input("\nEnter a keyword or date to search: ").lower()
        found = False
        
        try:
            with open(self.filename, "r") as file:
                entries = file.read().strip().split("\n\n")
                
                print("\n--- Matching Entries ---")
                for item in entries:
                    if keyword in item.lower():
                        print(item + "\n")
                        found = True
                
                if not found:
                    print(f"No entries were found for the keyword: {keyword}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def delete_all_entries(self):
        """Deletes the entire journal file after confirmation."""
        if not os.path.exists(self.filename):
            print("\nNo journal entries to delete.")
            return

        confirm = input("\nAre you sure you want to delete all entries? (yes/no): ").lower()
        if confirm == "yes":
            try:
                os.remove(self.filename)
                print("All journal entries have been deleted.")
            except Exception as e:
                print(f"Error deleting file: {e}")
        else:
            print("Deletion cancelled.")

def main():
    manager = JournalManager()
    
    while True:
        print("\nWelcome to Personal Journal Manager!")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")
        
        choice = input("\nPlease select an option: ")
        
        if choice == '1':
            manager.add_entry()
        elif choice == '2':
            manager.view_all_entries()
        elif choice == '3':
            manager.search_entry()
        elif choice == '4':
            manager.delete_all_entries()
        elif choice == '5':
            print("Thank you for using Personal Journal Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid option from the menu.")

if __name__ == "__main__":
    main()
