import unittest
from io import StringIO
import sys

from refactored.library_system import LibrarySystem


class TestLibrarySystem(unittest.TestCase):
    def setUp(self):
        self.lib = LibrarySystem()

    def capture_output(self, func, *args):
        captured = StringIO()
        sys.stdout = captured
        func(*args)
        sys.stdout = sys.__stdout__
        return captured.getvalue()

    def test_register_user_and_find(self):
        self.lib.register_user("Alice", "alice@example.com", 25)
        user = self.lib.users[0]
        self.assertEqual(user.name, "Alice")
        self.assertEqual(user.email, "alice@example.com")

    def test_add_book_and_find(self):
        self.lib.add_book("1984", "Orwell", 1949)
        book = self.lib.books[0]
        self.assertEqual(book.title, "1984")
        self.assertTrue(book.available)

    def test_borrow_book_successful(self):
        self.lib.register_user("Alice", "alice@example.com", 25)
        self.lib.add_book("1984", "Orwell", 1949)

        output = self.capture_output(self.lib.borrow_book, "Alice", "1984")

        self.assertIn("Alice borrowed 1984", output)
        self.assertFalse(self.lib.books[0].available)

    def test_borrow_book_user_not_found(self):
        self.lib.add_book("1984", "Orwell", 1949)
        output = self.capture_output(self.lib.borrow_book, "Ghost", "1984")
        self.assertIn("User not found", output)

    def test_borrow_book_not_available(self):
        self.lib.register_user("Alice", "alice@example.com", 25)
        self.lib.add_book("1984", "Orwell", 1949)
        self.lib.books[0].mark_unavailable()

        output = self.capture_output(self.lib.borrow_book, "Alice", "1984")
        self.assertIn("Book not available", output)

    def test_return_book_successful(self):
        self.lib.register_user("Alice", "alice@example.com", 25)
        self.lib.add_book("1984", "Orwell", 1949)
        self.lib.borrow_book("Alice", "1984")

        output = self.capture_output(self.lib.return_book, "Alice", "1984")

        self.assertIn("Alice returned 1984", output)
        self.assertTrue(self.lib.books[0].available)

    def test_return_book_user_not_found(self):
        output = self.capture_output(self.lib.return_book, "Ghost", "1984")
        self.assertIn("User not found", output)

    def test_return_book_not_borrowed(self):
        self.lib.register_user("Alice", "alice@example.com", 25)
        output = self.capture_output(self.lib.return_book, "Alice", "1984")
        self.assertIn("User has not borrowed any books", output)

