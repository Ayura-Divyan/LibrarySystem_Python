import csv

#Initialised dictionaries to load the data to
books = {}
student = {}
transaction = {}

def load_book():
    """Used to load the book.csv files into python memory"""
    try:
        with open('../data/book.csv', encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile) #Loads the csv file into a variable

            next(reader) #Skips the header row

            for row in reader:
                #Initialise the rows to separate indexes
                if len(row) == 6:
                    book_id = row[0]
                    isbn = row[1]
                    title = row[2]
                    copies = row[3]
                    availability = row[4]
                    price = row[5]

                    #Initialise dictionary
                    books[book_id] = {"title": title, "isbn": isbn, "copies": int(copies), "availability": availability, "price": float(price)}

            print("Books loaded")
    except FileNotFoundError: #Catch
        print("Books file not found")

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

            print("Students loaded")
    except FileNotFoundError: #Catch
        print("Students file not found")

def load_transaction():
    """Used to load the transactions.csv files into python memory"""
    try:
        with open('../data/transactions.csv', encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile) #Loads the csv file into a variable

            next(reader) #Skips the header row

            for row in reader:
                if len(row) == 2:
                    #Initialise the rows to separate indexes
                    transaction_id = row[0]
                    date = row[1]
                    book_id = row[2]
                    student_id = row[3]
                    transaction_type = row[4]

                    #Initialise dictionary
                    transaction[transaction_id] = {"date": date, "book_id": book_id, "student_id": student_id, "type": transaction_type}

            print("Transactions loaded")
    except FileNotFoundError: #Catch
        print("Transaction file not found")

#Start script
if __name__ == "__main__":
    load_book()
    load_student()
    load_transaction()

    print(books)
    print(student)
    print(transaction)