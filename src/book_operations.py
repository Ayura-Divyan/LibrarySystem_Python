from validators import book_validator
import menu_cli

def edit_book(search_id, books):
    """
    This is to edit the information of a book
    :param search_id:
    :param books:
    :return:
    """
    if search_id not in books:
        print("Book not found")
        menu_cli.book_menu(books)
    print(f"\n---Editing book {search_id}---\n")
    while True:  # Input new ISBN
        new_isbn = input("Enter ISBN: ")
        if not book_validator.isbn_valid(new_isbn):
            print("Error: Invalid ISBN. Please try again.")
            continue
        break  # If the ISBN passes all the validation the while loop breaks

    while True:  # Input new Tile
        new_book_title = input("Enter book title: ").upper()
        if not book_validator.title_valid(new_book_title):
            print("Error: Invalid book title. Please try again.")
            continue
        break  # If the title passes all the validation the while loop breaks

    while True: # Input New Price
        new_price = input("Enter price of the book: ")
        if not book_validator.price_valid(new_price):
            print("Error: Invalid price. Please try again.")
            continue
        break # If the number of copies passes all the validation the while loop breaks


    books[search_id]['isbn'] = new_isbn
    books[search_id]['title'] = new_book_title
    books[search_id]['price'] = new_price

    print(f"Success: Book {search_id} has been updated!")

def delete_book(search_id, books):
    if search_id not in books:
        print("Book not found")
        menu_cli.book_menu(books)

    books.pop(search_id)
    print(f"Success: Book {search_id} has been deleted!")