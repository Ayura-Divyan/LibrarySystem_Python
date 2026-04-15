#This module has methods for the for adding data to the database

from datetime import datetime
import validators

def add_book(book_dict):
    """
    Adds a book to the book dictionary
    :param book_dict:
    :return book_dict:
    """
    print("\n---Add a book---")

    while True: # Input booking ID
        book_id = input("Enter book id: ")
        if  not validators.id_validator.is_unique(book_id, "../data/book.csv"):
            print("Error: Booking ID already exists. Please try again.")
            continue

        if not validators.id_validator.booking_id_validator(book_id):
            print("Error: Invalid booking ID. Please try again.")
            continue
        break # If the booking id passes all the validation the while loop breaks

    while True: # Input ISBN
        isbn = input("Enter ISBN: ")
        if not validators.book_validator.isbn_valid(isbn):
            print("Error: Invalid ISBN. Please try again.")
            continue
        break # If the ISBN passes all the validation the while loop breaks

    while True: # Input Tile
        book_title = input("Enter book title: ")
        if not validators.book_validator.title_valid(book_title):
            print("Error: Invalid book title. Please try again.")
            continue
        break # If the title passes all the validation the while loop breaks

    while True:
        num_copies = input("Enter number of copies: ")
        if not validators.book_validator.copy_valid(num_copies):
            print("Error: Invalid number of copies. Please try again.")
            continue
        break # If the number of copies passes all the validation the while loop breaks

    available_copies = num_copies

    while True:
        price = input("Enter price of the book: ")
        if not validators.book_validator.price_valid(price):
            print("Error: Invalid price. Please try again.")
            continue
        break # If the number of copies passes all the validation the while loop breaks

    book_dict[book_id] = {
        "isbn": isbn,
        "title": book_title,
        "copies": int(num_copies),
        "availability": int(available_copies),
        "price": float(price)
    }

    return book_dict

def add_student(student_dict):
    """
    Adds students to the book dictionary
    :param student_dict:
    :return student_dict:
    """
    print("\n---Add students---")

    while True: # Input student ID
        student_id = input("Enter student ID: ")

        if not validators.id_validator.is_unique(student_id, "student.csv"):
            print("Error: Student ID already exists. Please try again.")
            continue
        break

    while True: # Input first name
        first_name = input("Enter first name: ")

        if not validators.string_validator.first_name_valid(first_name):
            print("Error: Invalid first name. Please try again.")
            continue
        break

    student_dict[student_id] = {
        "first_name": first_name
    }
    return student_dict