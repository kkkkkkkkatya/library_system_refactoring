# 📄 Журнал змін (Refactoring Log)

## [1] Technique: Replace Data Clumps + Primitive Obsession

**Before**:
Книги та користувачі описувалися словниками з набором полів.

**After**:
Введено класи `Book` і `User`. Замість словників з полями тепер використовуються повноцінні об'єкти з методами.

**Benefits**:
- Легше додавати методи (`mark_available`, `__repr__`)
- Можна перевіряти дані при ініціалізації
- Читабельніший код

## [2] Technique: Extract Method — find_book_by_title

**Before**: пошук книги реалізовувався прямо у методі borrow_book
**After**: винесено у окремий метод в BookService

## [3] Technique: Extract Class / Move Method — BookService, UserService

**Before**: вся логіка пошуку була всередині LibrarySystem
**After**: створено окремі сервіси для роботи з книгами і користувачами

**Benefits**:
- Вищий рівень абстракції
- Менше відповідальності на LibrarySystem
- Код легше тестувати та підтримувати

## [4] Technique: Replace Nested Conditional with Guard Clauses

**Before**: вкладені if/else перевірки
**After**: перевірки винесено в guard clauses

## [5] Technique: Extract Class — BorrowingManager

**Before**: позичені книги зберігались у словнику (Dict[str, List[Book]])
**After**: створено клас BorrowingManager + клас Borrowing

**Benefits**:
- Краще структурування даних
- Простіший доступ до позичених книг
- Можливість гнучко змінювати логіку в майбутньому

## [6] Add basic unit tests with edge-cases
- test borrowing manager
- test library system
- test services
