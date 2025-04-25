class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def mark_unavailable(self):
        self.available = False

    def mark_available(self):
        self.available = True

    def __repr__(self):
        return f"<Book {self.title} ({self.year})>"
