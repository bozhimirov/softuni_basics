searched_book = input()
current_book = ""
book_counter = 0
while current_book != searched_book:
    current_book = input()
    if current_book == "No More Books":
        break
    book_counter += 1
if searched_book == current_book:
    book_counter -= 1
    print(f"You checked {book_counter} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {book_counter} books.")
