class Book:
    

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"


class Library:
    

    def __init__(self):
        self.books = []

    def add_book(self, book):
        
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, isbn):
    
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book '{book.title}' removed from the library.")
                return
        print(f"No book found with ISBN {isbn}.")

    def list_books(self):
        
        if not self.books:
            return ["No books in the library."]
        return [book.display_info() for book in self.books]


book1 = Book("1984", "George Orwell", "12345")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "67890")

library = Library()
library.add_book(book1)
library.add_book(book2)

print("\nLibrary contents:")
for info in library.list_books():
    print(info)

library.remove_book("12345")

print("\nLibrary contents after removal:")
for info in library.list_books():
    print(info)
