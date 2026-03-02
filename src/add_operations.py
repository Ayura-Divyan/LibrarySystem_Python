#This module has methods for the for adding data to the database

import csv
import validators

def add_book(book_dict):
    print("\n---Add a book---")

    while True:
        book_id = input("Enter book id: ")
        if  not validators.id_validator.is_unique(book_id, "book.csv"):
            print("Error: Booking ID already exists. Please try again.")
            continue

        if not validators.id_validator.booking_id_validator(book_id):
            print("Error: Invalid booking ID. Please try again.")
            continue
        break #If the booking id passes all the validation the while loop breaks