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


def view_books(books):
    print("\n-----------------------------------------------------------------------------------------")
    print("LIBRARY INVENTORY".center(85))
    print("\n-----------------------------------------------------------------------------------------")

    if not books:
        print("Error: No books currently exist in the database.")
        print("\n-----------------------------------------------------------------------------------------")
        return

    print(f"{'BOOK ID':<10} | {'TITLE':<25} | {'ISBN':<15} | {'COPIES':<8} | {'STOCK':<8} | {'PRICE':<10}")
    print("\n-----------------------------------------------------------------------------------------")

    for book_id, details in books.items():
        title = details['title']
        isbn = details['isbn']
        copies = details['copies']
        availability = details['availability']
        price = details['price']

        if len(title) > 22:
            title = title[:19] + "..."

        print(f"{book_id:<10} | {title:<25} | {isbn:<15} | {copies:<8} | {availability:<8} | ${price:<9}")

def search_book(search_id, books):
    if search_id not in books:
        print("Book not found")
        menu_cli.book_menu(books)
    print(f"\n---Searching book {search_id}---\n")

    print(f"{'BOOK ID':<10} | {'TITLE':<25} | {'ISBN':<15} | {'COPIES':<8} | {'STOCK':<8} | {'PRICE':<10}")
    print("\n-----------------------------------------------------------------------------------------")
    title = books[search_id]['title']
    isbn = books[search_id]['isbn']
    copies = books[search_id]['copies']
    availability = books[search_id]['availability']
    price = books[search_id]['price']
    if len(title) > 22:
        title = books[search_id]["title"][:19] + "..."

    print(f"{search_id:<10} | {title:<25} | {isbn:<15} | {copies:<8} | {availability:<8} | ${price:<9}")