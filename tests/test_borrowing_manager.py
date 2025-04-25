import unittest
from refactored.models.user_model import User
from refactored.models.book_model import Book
from refactored.services.borrowing_manager import BorrowingManager


class TestBorrowingManager(unittest.TestCase):
    def setUp(self):
        self.manager = BorrowingManager()
        self.user1 = User("Olena", "olenas@mail.com", 23)
        self.user2 = User("Ivan", "ivans@mail.com", 23)
        self.book1 = Book("Python Tricks", "Dan Bader", 2003)
        self.book2 = Book("Fluent Python", "Luciano Ramalho", 1978)
        self.book3 = Book("Clean Code", "Robert C. Martin", 2000)

    def test_add_borrowing(self):
        self.manager.add_borrowing(self.user1, self.book1)
        self.assertEqual(len(self.manager.borrowings), 1)
        self.assertEqual(self.manager.borrowings[0].book.title, "Python Tricks")

    def test_return_book_success(self):
        self.manager.add_borrowing(self.user1, self.book1)
        returned = self.manager.return_book(self.user1, "Python Tricks")
        self.assertEqual(returned.title, "Python Tricks")
        self.assertEqual(len(self.manager.borrowings), 0)

    def test_return_book_not_found(self):
        self.manager.add_borrowing(self.user1, self.book1)
        result = self.manager.return_book(self.user1, "Nonexistent Book")
        self.assertIsNone(result)

    def test_return_book_twice(self):
        self.manager.add_borrowing(self.user1, self.book1)
        returned1 = self.manager.return_book(self.user1, "Python Tricks")
        returned2 = self.manager.return_book(self.user1, "Python Tricks")
        self.assertIsNotNone(returned1)
        self.assertIsNone(returned2)
        self.assertEqual(len(self.manager.borrowings), 0)

    def test_multiple_users_borrow_same_book_instance(self):
        self.manager.add_borrowing(self.user1, self.book1)
        self.manager.add_borrowing(self.user2, self.book1)
        self.assertEqual(len(self.manager.borrowings), 2)
        self.assertTrue(self.manager.has_borrowed(self.user1))
        self.assertTrue(self.manager.has_borrowed(self.user2))

    def test_has_borrowed_true(self):
        self.manager.add_borrowing(self.user1, self.book1)
        self.assertTrue(self.manager.has_borrowed(self.user1))

    def test_has_borrowed_false(self):
        self.manager.add_borrowing(self.user1, self.book1)
        self.assertFalse(self.manager.has_borrowed(self.user2))

    def test_get_borrowed_books(self):
        self.manager.add_borrowing(self.user1, self.book1)
        self.manager.add_borrowing(self.user1, self.book2)
        books = self.manager.get_borrowed_books(self.user1)
        self.assertEqual(len(books), 2)
        self.assertEqual(books[0].title, "Python Tricks")
        self.assertEqual(books[1].title, "Fluent Python")

    def test_get_borrowed_books_empty(self):
        books = self.manager.get_borrowed_books(self.user1)
        self.assertEqual(books, [])

    def test_borrow_and_return_multiple_books(self):
        self.manager.add_borrowing(self.user1, self.book1)
        self.manager.add_borrowing(self.user1, self.book2)
        self.manager.add_borrowing(self.user1, self.book3)

        self.assertEqual(len(self.manager.get_borrowed_books(self.user1)), 3)

        self.manager.return_book(self.user1, "Fluent Python")
        books_left = self.manager.get_borrowed_books(self.user1)

        self.assertEqual(len(books_left), 2)
        titles = [book.title for book in books_left]
        self.assertNotIn("Fluent Python", titles)
