from datetime import datetime
import validators

def issue_book(books, students, transactions):
    """
    Used to issue books to students
    :param books:
    :param students:
    :param transactions:
    :return:
    """
    print("\n---Issue book---")

    book_id = input("Enter book id: ").upper()
    if book_id not in books:
        print("Error: Invalid book ID.")
        return
    elif int(books[book_id]["availability"]) < 1:
        print("Error: There are no copies of this book available.")
        return

    student_id = input("Enter student ID: ")
    if student_id not in students:
        print("Error: Invalid student ID.")
        return

    # Multiple copy issuance check
    for transaction_id, details in transactions.items():
        if details["student_id"] == student_id and details["book_id"] == book_id:
            if details["type"] == "1":
                print("Error: Book already issued. This student already has a copy.")
                return

    # Date input and validation
    while True:
        date_str = input("Enter issue date (DD/MM/YYYY): ")
        try:
            datetime.strptime(date_str, "%d/%m/%Y")
            break
        except ValueError:
            print("Error: Invalid date format. Please use DD/MM/YYYY.")

    # Generate a new Transaction ID
    new_transaction_id = f"T{len(transactions) + 1:03}"

    # Add to dictionary
    transactions[new_transaction_id] = {
        "date":date_str,
        "book_id": book_id,
        "student_id": student_id,
        "type": "1"
    }

    # Reduce the number of available copies
    books[book_id]["availability"] = int(books[book_id]["availability"]) - 1


    print("Book issued successfully.")


def return_book(books, students, transactions):
    """
    Used to return books from students
    :param books:
    :param students:
    :param transactions:
    :return:
    """
    print("\n---Return book---")

    # Validate IDs
    book_id = input("Enter book id: ").upper()
    if book_id not in books:
        print("Error: Invalid book ID.")
        return

    student_id = input("Enter student ID: ")
    if student_id not in students:
        print("Error: Invalid student ID.")
        return

    # Date input and validation
    while True:
        date_str = input("Enter return date (DD/MM/YYYY): ")
        try:
            datetime.strptime(date_str, "%d/%m/%Y")
            break
        except ValueError:
            print("Error: Invalid date format. Please use DD/MM/YYYY.")
    # Find the Active Issue
    found_transaction = None
    for trans_id, details in transactions.items():
        if (details["book_id"] == book_id and
                details["student_id"] == student_id and
                details["type"] == "1"):
            found_transaction = details
            break

    if found_transaction:
        found_transaction["type"] = "2"
        found_transaction["date"] = date_str
        books[book_id]["availability"] = int(books[book_id]["availability"]) + 1
        print("Book returned successfully.")
    else:
        print("Error: No active issue record found for this student and book.")