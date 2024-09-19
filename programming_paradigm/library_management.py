# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability
    
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True  # Book successfully checked out
        return False  # Book is already checked out
    
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True  # Book successfully returned
        return False  # Book was not checked out

    def is_available(self):
        return not self._is_checked_out  # Returns True if book is available

    def __str__(self):
        status = "Available" if self.is_available() else "Checked Out"
        return f"'{self.title}' by {self.author} - {status}"


class Library:
    def __init__(self):
        self._books = []  # Private list to store Book objects
    
    def add_book(self, title, author):
        new_book = Book(title, author)
        self._books.append(new_book)
        print(f"Book '{title}' by {author} added to the library.")
    
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Book '{title}' has been checked out.")
                    return
                else:
                    print(f"Book '{title}' is already checked out.")
                    return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Book '{title}' has been returned.")
                    return
                else:
                    print(f"Book '{title}' was not checked out.")
                    return
        print(f"Book '{title}' not found in the library.")

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            print("Available Books:")
            for book in available_books:
                print(f"- {book}")
        else:
            print("No books are currently available.")

# Example usage (this part can be excluded in the script):
if __name__ == "__main__":
    library = Library()
    
    # Adding books to the library
    library.add_book("1984", "George Orwell")
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
    
    # Listing available books
    library.list_available_books()
    
    # Checking out a book
    library.check_out_book("1984")
    
    # Listing available books after checking one out
    library.list_available_books()
    
    # Returning a book
    library.return_book("1984")
    
    # Listing available books after returning
    library.list_available_books()
