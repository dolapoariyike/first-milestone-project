class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year, isbn):
        new_book = {
            'Title': title,
            'Author': author,
            'Year': year,
            'ISBN': isbn,
            'Available': True
        }
        self.books.append(new_book)
        print(f'Book "{title}" added successfully!')

    def view_books(self):
        if not self.books:
            print("No books in the library.")
            return
        for book in self.books:
            availability = "Available" if book['Available'] else "Not Available"
            print(f'Title: {book["Title"]}, Author: {book["Author"]}, Year: {book["Year"]}, ISBN: {book["ISBN"]}, Status: {availability}')

    def update_book(self, isbn):
        for book in self.books:
            if book['ISBN'] == isbn:
                book['Title'] = input("Enter new title: ")
                book['Author'] = input("Enter new author: ")
                book['Year'] = int(input("Enter new year of publication: "))
                print(f'Book with ISBN {isbn} updated successfully!')
                return
        print(f'No book found with ISBN {isbn}.')

    def delete_book(self, isbn):
        for book in self.books:
            if book['ISBN'] == isbn:
                self.books.remove(book)
                print(f'Book with ISBN {isbn} deleted successfully!')
                return
        print(f'No book found with ISBN {isbn}.')

    def search_book(self, title):
        for book in self.books:
            if book['Title'].lower() == title.lower():
                availability = "Available" if book['Available'] else "Not Available"
                print(f'Title: {book["Title"]}, Author: {book["Author"]}, Year: {book["Year"]}, ISBN: {book["ISBN"]}, Status: {availability}')
                return
        print(f'No book found with the title "{title}".')

    def borrow_book(self, isbn):
        for book in self.books:
            if book['ISBN'] == isbn:
                if book['Available']:
                    book['Available'] = False
                    print(f'You have borrowed "{book["Title"]}".')
                else:
                    print(f'The book "{book["Title"]}" is not available for borrowing.')
                return
        print(f'No book found with ISBN {isbn}.')

    def return_book(self, isbn):
        for book in self.books:
            if book['ISBN'] == isbn:
                if not book['Available']:
                    book['Available'] = True
                    print(f'You have returned "{book["Title"]}".')
                else:
                    print(f'The book "{book["Title"]}" was not borrowed.')
                return
        print(f'No book found with ISBN {isbn}.')

def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Search Book")
        print("6. Borrow Book")
        print("7. Return Book")
        print("8. Exit")

        choice = input("Select an option (1-8): ")

        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            year = int(input("Enter year of publication: "))
            isbn = input("Enter ISBN: ")
            library.add_book(title, author, year, isbn)
        elif choice == '2':
            library.view_books()
        elif choice == '3':
            isbn = input("Enter ISBN of the book to update: ")
            library.update_book(isbn)
        elif choice == '4':
            isbn = input("Enter ISBN of the book to delete: ")
            library.delete_book(isbn)
        elif choice == '5':
            title = input("Enter the exact title of the book to search: ")
            library.search_book(title)
        elif choice == '6':
            isbn = input("Enter ISBN of the book to borrow: ")
            library.borrow_book(isbn)
        elif choice == '7':
            isbn = input("Enter ISBN of the book to return: ")
            library.return_book(isbn)
        elif choice == '8':
            print("Exiting the library management system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


main()
