import csv
import os

# Base csv relative file directory
DATA_DIR = "../data/"

def _load_base_data(filename, primary_header, expected_columns):
    """
    Handles loading data from a CSV file
    :param filename:
    :param primary_header:
    :param expected_columns:
    :return:
    """
    data_dict = {}
    filepath = os.path.join(DATA_DIR, filename)

    try:
        with open(filepath, mode="r", encoding="utf-8", newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if len(row) != expected_columns:
                    continue

                # Extract the ID to use as the main dictionary key
                item_id = row.pop(primary_header)
                data_dict[item_id] = row
            return data_dict
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return {}

def load_book():
    """Used to load the book.csv files into python memory"""
    # Maps the CSV header names to your preferred dictionary keys
    raw_data = _load_base_data("book.csv", "Book id", 6)

    for booking_id, details in raw_data.items():
        # Type

def load_student():
    """Used to load the student.csv files into python memory"""
    try:
        with open('../data/student.csv', encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile) #Loads the csv file into a variable

            next(reader) #Skips the header row

            for row in reader:
                if len(row) == 2:
                    #Initialise the rows to separate indexes
                    student_id = row[0]
                    first_name = row[1]

                    #Initialise dictionary
                    student[student_id] = {"first_name": first_name}
                else:
                    raise ValueError

            print("Students loaded")
            return student
    except FileNotFoundError: #Catch
        print("Students file not found")
    except ValueError:
        print("Columns exceeded (expected 2 columns)")

def load_transaction():
    """Used to load the transactions.csv files into python memory"""
    try:
        with open('../data/transactions.csv', encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile) #Loads the csv file into a variable

            next(reader) #Skips the header row

            for row in reader:
                if len(row) == 5:
                    #Initialise the rows to separate indexes
                    transaction_id = row[0]
                    date = row[1]
                    book_id = row[2]
                    student_id = row[3]
                    transaction_type = row[4]

                    #Initialise dictionary
                    transaction[transaction_id] = {"date": date, "book_id": book_id, "student_id": student_id, "type": transaction_type}
                else:
                    raise ValueError
            print("Transactions loaded")
            return transaction
    except FileNotFoundError: #Catch
        print("Transaction file not found")
    except ValueError:
        print("Columns exceeded (expected 5 columns)")