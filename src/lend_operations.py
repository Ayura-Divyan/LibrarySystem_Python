from datetime import datetime

def issue_book(books, students, transactions):
    print("\n---Issue book---")

    while True:  # Checks if the Book ID exists in the dictionary
        book_id = input("Enter book id: ")
        if book_id not in books:
            print("Error: Invalid book ID. Please try again.")
            continue
        break

    while True:  # Checks if the student ID exists in the dictionary
        student_id = input("Enter student ID: ")
        if student_id not in students:
            print("Error: Invalid student ID. Please try again.")
            continue
        break

    # Multiple copy issuance check
    for transaction_id, details in transactions.items():
        if details["student_id"] == student_id and details["book_id"] == book_id:
            if details["type"] == "1":
                print("Error: Book already issued. This student already has a copy.")
                return

    # Date input and validation
    while True:
        date_str = input("Enter book date (DD/MM/YYYY): ")
        if not datetime.strptime(date_str, "%d/%m/%Y"):
            print("Error: Invalid date format. Please try again.")
            continue
        break
