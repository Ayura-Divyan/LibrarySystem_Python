import csv

# Initialised dictionaries to load the data to
books = {}
student = {}
transaction = {}


def load_book():
    """Used to load the book.csv files into python memory using DictReader"""
    try:
        with open('../data/book.csv', mode="r", encoding="utf-8", newline='') as csvfile:
            # DictReader uses the first row of the CSV as keys
            reader = csv.DictReader(csvfile)

            for row in reader:
                # Instead of row[0], use the header name 'book_id'
                book_id = row['book_id']

                # Assign values using header names
                books[book_id] = {
                    "title": row['title'],
                    "isbn": row['isbn'],
                    "copies": int(row['copies']),
                    "availability": row['availability'],
                    "price": float(row['price'])
                }

            print("Books loaded")
            return books
    except FileNotFoundError:
        print("Books file not found")
    except KeyError as e:
        print(f"Missing column in book.csv: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def load_student():
    """Used to load the student.csv files into python memory using DictReader"""
    try:
        with open('../data/student.csv', mode="r", encoding="utf-8", newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                # Use the header name 'student_id'
                student_id = row['student_id']

                student[student_id] = {
                    "first_name": row['first_name']
                }

            print("Students loaded")
            return student
    except FileNotFoundError:
        print("Students file not found")
    except KeyError as e:
        print(f"Missing column in student.csv: {e}")


def load_transaction():
    """Used to load the transactions.csv files into python memory using DictReader"""
    try:
        with open('../data/transactions.csv', mode="r", encoding="utf-8", newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                # Use the header name 'transaction_id'
                transaction_id = row['transaction_id']

                transaction[transaction_id] = {
                    "date": row['date'],
                    "book_id": row['book_id'],
                    "student_id": row['student_id'],
                    "type": row['type']
                }

            print("Transactions loaded")
            return transaction
    except FileNotFoundError:
        print("Transaction file not found")
    except KeyError as e:
        print(f"Missing column in transactions.csv: {e}")