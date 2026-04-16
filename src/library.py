import warm_boot
from menu_cli import main_menu

print("Initializing Library Management System...")

# Dictionary Headers
book_headers = ['book_id', 'isbn', 'title', 'copies', 'availability', 'price']
student_headers = ['student_id', 'first_name']
trans_headers = ['transaction_id', 'date', 'book_id', 'student_id', 'type']

# Load dat
books = warm_boot.load_csv_data('book.csv', 'book_id', book_headers)
students = warm_boot.load_csv_data('student.csv', 'student_id', student_headers)
transactions = warm_boot.load_csv_data('transaction.csv', 'transaction_id', trans_headers)

# Start the main menu
main_menu(books, students, transactions)