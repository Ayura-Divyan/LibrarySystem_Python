from warm_boot import *

#Initialised dictionaries to load the data to
books = {}
student = {}
transaction = {}

#Start script
if __name__ == "__main__":
    books = load_book()
    student = load_student()
    transaction = load_transaction()

    print(books)
    print(student)
    print(transaction)