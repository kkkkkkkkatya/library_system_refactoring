class BookService:
    @staticmethod
    def find_book_by_title(books, title):
        for book in books:
            if book.title == title:
                return book
        return None
