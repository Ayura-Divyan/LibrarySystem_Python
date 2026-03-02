import csv

def is_unique(id_value, csv_file_name):
    """
    Checks if the value entered by user is unique compared to the CSV file.
    :param id_value: The user input to be validated
    :param csv_file_name: The name of the csv file
    :return: Boolean to validate the value
    """
    try:
        with open(f"../../data/{csv_file_name}", "r", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                if id_value in row:
                    raise ValueError #If the id already exists in the csv file it will raise the error
            return True
    except FileNotFoundError:
        print(f"Error: File '{csv_file_name}' could be not found.")
    except ValueError:
        print(f"Error: {id_value} is not unique")

def booking_id_validator(booking_id):
    """
    Checks if the characters consists of two letters and two digits
    :param booking_id:
    :return:
    """
    booking_id = str(booking_id)
    try:
        if len(booking_id) == 4 and booking_id[:2].isalpha() and booking_id[-2:].isdigit():
            return True
        else:
            raise ValueError #If the id doesn't meet the validation it will raise the error
    except ValueError:
        print(f"Error: {booking_id} is not a valid booking id.")

