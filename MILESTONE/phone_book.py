class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number):
        new_contact = {
            'Name': name,
            'Phone Number': phone_number,
            'Favorite': False
        }
        self.contacts.append(new_contact)
        print(f'Contact "{name}" added successfully!')

    def view_contacts(self):
        if not self.contacts:
            print("No contacts in the phone book.")
            return
        for contact in self.contacts:
            favorite_status = "Favorite" if contact['Favorite'] else "Not Favorite"
            print(f'Name: {contact["Name"]}, Phone Number: {contact["Phone Number"]}, Status: {favorite_status}')

    def update_contact(self, phone_number):
        for contact in self.contacts:
            if contact['Phone Number'] == phone_number:
                contact['Name'] = input("Enter new name: ")
                contact['Phone Number'] = input("Enter new phone number: ")
                print(f'Contact with phone number {phone_number} updated successfully!')
                return
        print(f'No contact found with phone number {phone_number}.')

    def delete_contact(self, phone_number):
        for contact in self.contacts:
            if contact['Phone Number'] == phone_number:
                self.contacts.remove(contact)
                print(f'Contact with phone number {phone_number} deleted successfully!')
                return
        print(f'No contact found with phone number {phone_number}.')

    def search_contact(self, name):
        for contact in self.contacts:
            if contact['Name'].lower() == name.lower():
                favorite_status = "Favorite" if contact['Favorite'] else "Not Favorite"
                print(f'Name: {contact["Name"]}, Phone Number: {contact["Phone Number"]}, Status: {favorite_status}')
                return
        print(f'No contact found with the name "{name}".')

    def mark_favorite(self, phone_number):
        for contact in self.contacts:
            if contact['Phone Number'] == phone_number:
                contact['Favorite'] = True
                print(f'Contact "{contact["Name"]}" marked as favorite.')
                return
        print(f'No contact found with phone number {phone_number}.')

    def unmark_favorite(self, phone_number):
        for contact in self.contacts:
            if contact['Phone Number'] == phone_number:
                contact['Favorite'] = False
                print(f'Contact "{contact["Name"]}" unmarked as favorite.')
                return
        print(f'No contact found with phone number {phone_number}.')

def main():
    phone_book = PhoneBook()
    while True:
        print("\nPhone Book Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contact")
        print("6. Mark Favorite")
        print("7. Unmark Favorite")
        print("8. Exit")

        choice = input("Select an option (1-8): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone_number = input("Enter phone number: ")
            phone_book.add_contact(name, phone_number)
        elif choice == '2':
            phone_book.view_contacts()
        elif choice == '3':
            phone_number = input("Enter phone number of the contact to update: ")
            phone_book.update_contact(phone_number)
        elif choice == '4':
            phone_number = input("Enter phone number of the contact to delete: ")
            phone_book.delete_contact(phone_number)
        elif choice == '5':
            name = input("Enter the exact name of the contact to search: ")
            phone_book.search_contact(name)
        elif choice == '6':
            phone_number = input("Enter phone number of the contact to mark as favorite: ")
            phone_book.mark_favorite(phone_number)
        elif choice == '7':
            phone_number = input("Enter phone number of the contact to unmark as favorite: ")
            phone_book.unmark_favorite(phone_number)
        elif choice == '8':
            print("Exiting the phone book manager. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

main()
