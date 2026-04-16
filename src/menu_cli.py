from add_operations import *
from lend_operations import *
from warm_boot import save_csv_data
import book_operations as bop

def main_menu(books, students, transactions):
    """
    Runs the Main Menu CLI
    :param books:
    :param students:
    :param transactions:
    :return:
    """
    while True:
        print("\n------------------------------------------")
        print("Welcome to the Library Management System")
        print("------------------------------------------")

        print("1. Book Operations")
        print("2. Add Student")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Save and Exit")

        try:
            selection = int(input("\nEnter your choice: "))
        except ValueError:
            print("Error: Please enter a valid number.")
            continue

        if selection == 1:
            book_menu(books)

        elif selection == 2:
            add_student(students)

        elif selection == 3:
            issue_book(books, students, transactions)

        elif selection == 4:
            return_book(books, students, transactions)

        elif selection == 5:
            print("\nSaving database...")
            # Trigger your warm_boot save functions here
            save_csv_data('book.csv', books, 'book_id')
            save_csv_data('student.csv', students, 'student_id')
            save_csv_data('transaction.csv', transactions, 'transaction_id')
            print("System shutting down. Goodbye.")
            break  # Exits the loop, ending the program

        else:
            print("Error: Invalid choice. Please select a number from 1 to 5.")

def book_menu(books):
    """
    Runs the Book Menu CLI
    :param books:
    :return:
    """
    while True:
        print("\n------------------------------------------")
        print("Book Operations")
        print("------------------------------------------")
        print("1. Add Book")
        print("2. Edit book")
        print("3. Delete book (Not implemented)")
        print("4. View All Book Information (Not implemented)")
        print("5. Return to Main Menu")

        try:
            book_selection = int(input("\nEnter your choice: "))
        except ValueError:
            print("Error: Please enter a valid number.")
            continue

        if book_selection == 1:
            add_book(books)
            break
        elif book_selection == 2:
            edit_id = input("Enter book ID to edit: ").upper()
            bop.edit_book(edit_id, books)
            break
        elif book_selection == 5:
            return
        else:
            print("Feature under development. Returning to main menu.")
            break