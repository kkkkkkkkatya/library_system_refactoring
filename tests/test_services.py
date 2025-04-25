import unittest

from refactored.models.book_model import Book
from refactored.models.user_model import User
from refactored.services.book_service import BookService
from refactored.services.user_service import UserService


class TestUserService(unittest.TestCase):
    def test_find_user_by_name_found(self):
        users = [User("Alice", "alice@example.com", 25), User("Bob", "bob@example.com", 30)]
        user = UserService.find_user_by_name(users, "Bob")
        self.assertEqual(user.name, "Bob")

    def test_find_user_by_name_not_found(self):
        users = [User("Alice", "alice@example.com", 25)]
        user = UserService.find_user_by_name(users, "Charlie")
        self.assertIsNone(user)


class TestBookService(unittest.TestCase):
    def test_find_book_by_title_found(self):
        books = [Book("1984", "Orwell", 1949), Book("Dune", "Herbert", 1965)]
        book = BookService.find_book_by_title(books, "Dune")
        self.assertEqual(book.author, "Herbert")

    def test_find_book_by_title_not_found(self):
        books = [Book("1984", "Orwell", 1949)]
        book = BookService.find_book_by_title(books, "Dune")
        self.assertIsNone(book)
