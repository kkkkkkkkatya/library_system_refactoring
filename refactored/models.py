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


class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def __repr__(self):
        return f"<User {self.name}>"
