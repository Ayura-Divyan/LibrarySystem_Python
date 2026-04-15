#This module has methods for the for adding data to the database

import csv
import validators

def add_book(book_dict):
    print("\n---Add a book---")

    while True: # Input booking ID
        book_id = input("Enter book id: ")
        if  not validators.id_validator.is_unique(book_id, "book.csv"):
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