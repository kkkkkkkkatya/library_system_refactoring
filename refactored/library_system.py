from .models import Book, User
from .services.book_service import BookService
from .services.user_service import UserService


class LibrarySystem:
    def __init__(self):
        self.books = []
        self.users = []
        self.borrowed_books = {}

    def add_book(self, title, author, year):
        self.books.append(Book(title, author, year))

    def register_user(self, name, email, age):
        self.users.append(User(name, email, age))

    def borrow_book(self, user_name, book_title):
        user = UserService.find_user_by_name(self.users, user_name)
        book = BookService.find_book_by_title(self.books, book_title)

        if not user:
            print("User not found")
            return

        if not book:
            print("Book not found")
            return

        if not book.available:
            print("Book not available")
            return

        book.mark_unavailable()
        self.borrowed_books.setdefault(user.name, []).append(book)
        print(f"{user.name} borrowed {book.title}")

    def return_book(self, user_name, book_title):
        user = UserService.find_user_by_name(self.users, user_name)
        if not user:
            print("User not found")
            return

        if user.name not in self.borrowed_books:
            print("User has not borrowed any books")
            return

        for book in self.borrowed_books[user.name]:
            if book.title == book_title:
                book.mark_available()
                self.borrowed_books[user.name].remove(book)
                print(f"{user.name} returned {book.title}")
                return

        print("Book not found in user's borrowed list")
