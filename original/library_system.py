class LibrarySystem:
    def __init__(self):
        self.books = []
        self.users = []
        self.borrowed_books = {}

    def add_book(self, title, author, year):
        self.books.append({"title": title, "author": author, "year": year, "available": True})

    def register_user(self, name, email, age):
        self.users.append({"name": name, "email": email, "age": age})

    def borrow_book(self, user_name, book_title):
        for book in self.books:
            if book["title"] == book_title:
                if book["available"]:
                    book["available"] = False
                    if user_name not in self.borrowed_books:
                        self.borrowed_books[user_name] = []
                    self.borrowed_books[user_name].append(book)
                    print(f"{user_name} borrowed {book_title}")
                    return
                else:
                    print("Book not available")
                    return
        print("Book not found")

    def return_book(self, user_name, book_title):
        if user_name in self.borrowed_books:
            for book in self.borrowed_books[user_name]:
                if book["title"] == book_title:
                    book["available"] = True
                    self.borrowed_books[user_name].remove(book)
                    print(f"{user_name} returned {book_title}")
                    return
        print("Book not found in user's borrowed list")
