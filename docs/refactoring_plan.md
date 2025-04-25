# 📘 План рефакторингу LibrarySystem

## Ціль
Покращити читабельність, підтримуваність та масштабованість системи керування бібліотекою.

## Проблеми:
1. Long Method: `borrow_book`, `return_book` роблять багато логіки.
2. Duplicated Code: пошук книги дублюється.
3. Primitive Obsession: словники замість об'єктів.
4. Data Clumps: багато параметрів в одному місці.
5. Feature Envy: методи маніпулюють даними інших класів.

## Заплановані техніки:
- Extract Method
- Replace Magic Number with Constant
- Introduce Class
- Replace Data Clumps with Object
- Move Method
- Encapsulate Collection
- Replace Type Code with Subclasses
- Remove Dead Code
- Replace Temp with Query
- Rename Method
