class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def __repr__(self):
        return f"<User {self.name}>"
