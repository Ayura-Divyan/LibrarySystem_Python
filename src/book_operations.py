from validators import book_validator

def edit_book(search_id, books):
    print(f"---Editing book {search_id}---")
    while True:  # Input new ISBN
        new_isbn = input("Enter ISBN: ")
        if not book_validator.isbn_valid(new_isbn):
            print("Error: Invalid ISBN. Please try again.")
            continue
        break  # If the ISBN passes all the validation the while loop breaks

    while True:  # Input new Tile
        new_book_title = input("Enter book title: ")
        if not book_validator.title_valid(new_book_title):
            print("Error: Invalid book title. Please try again.")
            continue
        break  # If the title passes all the validation the while loop breaks


    for book_in, details in books.items():
        if details['book_id'] == search_id:
            details['book_title'] = new_book_title
            details['book_isbn'] = new_isbn