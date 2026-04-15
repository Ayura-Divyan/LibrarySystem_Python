from warm_boot import *

#Initialised dictionaries to load the data to
books = {}
student = {}
transaction = {}

#Start script
if __name__ == "__main__":
books = load_csv_data("book.csv", "book_id", 6)
student = load_csv_data("student.csv", "student_id", 2)
transaction = load_csv_data("transaction.csv", "transaction_id", 5)

