from ..models.borrowing_model import Borrowing


class BorrowingManager:
    def __init__(self):
        self.borrowings = []

    def add_borrowing(self, user, book):
        self.borrowings.append(Borrowing(user, book))

    def return_book(self, user, book_title):
        for b in self.borrowings:
            if b.user == user and b.book.title == book_title:
                self.borrowings.remove(b)
                return b.book
        return None

    def has_borrowed(self, user):
        return any(b.user == user for b in self.borrowings)

    def get_borrowed_books(self, user):
        return [b.book for b in self.borrowings if b.user == user]
