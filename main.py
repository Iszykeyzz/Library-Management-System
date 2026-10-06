class Book:
    def __init__(self, author, title, isbn):
        self.author = author
        self.title = title
        self.isbn = isbn
        self._is_borrowed = False

    @property
    def is_borrowed(self):
        return self._is_borrowed

    def borrow(self):
        if self._is_borrowed:
            raise ValueError (f"The book '{self.title}' is already borrowed.")
        else:
            self._is_borrowed = True
            return f"You have borrowed '{self.title}' by {self.author}."
        
    def return_book(self):
        if not self._is_borrowed:
            raise ValueError (f"The book '{self.title}' is not currently borrowed.")
        else:
            self._is_borrowed = False
            return f"You have returned '{self.title}' by {self.author}."

    def __str__(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) is {'Borrowed' if self._is_borrowed else 'Available'}"

book1 = Book("George Orwell", "1984", "9780451524935")

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_borrowed:
            raise ValueError(f"{self.name} cannot borrow '{book.title}' because it is already borrowed.")
        else:
            book.borrow()
            self.borrowed_books.append(book)

    def return_book(self, book):
        if book not in self.borrowed_books:
            raise ValueError(f"{self.name} cannot return '{book.title}' because it was not borrowed by them.")
        else:
            book.return_book()
            self.borrowed_books.remove(book)

    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id}), Borrowed Books: {len(self.borrowed_books)}"
    
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        if self.find_book(book.isbn):
            raise ValueError(f"The book with ISBN {book.isbn} already exists in the library.")
        self.books.append(book)

    def register_member(self, member):
        if self.find_member(member.member_id):
            raise ValueError(f"A member with ID {member.member_id} already exists.")
        self.members.append(member)

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def display_available_books(self):
        if not self.books:
            return "No books in the library."
        elif all(book.is_borrowed for book in self.books):
            return "No available books in the library."
        else:
            return "\n".join(str(book) for book in self.books if not book.is_borrowed)

    def display_borrowed_books(self):
        if not self.books:
            return "No books in the library."
        else:
            return "\n".join(str(book) for book in self.books if book.is_borrowed)


book1 = Book("George Orwell", "1984", "9780451524935")
book2 = Book("J.R.R. Tolkien", "The Hobbit", "9780547928227")
book3 = Book("Chinua Achebe", "Things Fall Apart", "9780385474542")

member_1 = Member("Israel", "001")
member_2 = Member("John", "002")

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.register_member(member_1)
library.register_member(member_2)

member_1.borrow_book(book1)
try:
    member_2.borrow_book(book1)
except ValueError as e:
    print(e)
print(book1)
print(library.display_available_books())

member_1.return_book(book1)
print(book1)
print(member_1)
try:
    member_2.return_book(book1)
except ValueError as e:
    print(e)

member_2.borrow_book(book1)
print(book1)