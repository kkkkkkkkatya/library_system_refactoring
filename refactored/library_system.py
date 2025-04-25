from models.user_model import User
from models.book_model import Book
from services.book_service import BookService
from services.user_service import UserService
from services.borrowing_manager import BorrowingManager


class LibrarySystem:
    def __init__(self):
        self.books = []
        self.users = []
        self.borrowing_manager = BorrowingManager()

    def add_book(self, title, author, year):
        self.books.append(Book(title, author, year))

    def register_user(self, name, email, age):
        self.users.append(User(name, email, age))

    def borrow_book(self, user_name, book_title):
        user = UserService.find_user_by_name(self.users, user_name)
        if not user:
            print("User not found")
            return

        book = BookService.find_book_by_title(self.books, book_title)
        if not book:
            print("Book not found")
            return

        if not book.available:
            print("Book not available")
            return

        book.mark_unavailable()
        self.borrowing_manager.add_borrowing(user, book)
        print(f"{user.name} borrowed {book.title}")

    def return_book(self, user_name, book_title):
        user = UserService.find_user_by_name(self.users, user_name)
        if not user:
            print("User not found")
            return

        if not self.borrowing_manager.has_borrowed(user):
            print("User has not borrowed any books")
            return

        returned_book = self.borrowing_manager.return_book(user, book_title)
        if returned_book:
            returned_book.mark_available()
            print(f"{user.name} returned {returned_book.title}")
        else:
            print("Book not found in user's borrowed list")
