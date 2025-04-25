import pytest
from original.library_system import LibrarySystem

@pytest.fixture
def system():
    ls = LibrarySystem()
    ls.add_book("1984", "George Orwell", 1949)
    ls.register_user("Alice", "alice@example.com", 30)
    return ls

def test_add_book(system):
    assert len(system.books) == 1

def test_register_user(system):
    assert len(system.users) == 1

def test_borrow_book(system, capsys):
    system.borrow_book("Alice", "1984")
    captured = capsys.readouterr()
    assert "Alice borrowed 1984" in captured.out
    assert system.books[0]["available"] is False

def test_return_book(system, capsys):
    system.borrow_book("Alice", "1984")
    system.return_book("Alice", "1984")
    captured = capsys.readouterr()
    assert "Alice returned 1984" in captured.out
    assert system.books[0]["available"] is True
