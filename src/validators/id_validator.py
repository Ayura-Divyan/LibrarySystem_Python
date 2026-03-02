import csv

def is_unique(id_value, csv_file_name):
    """
    Checks if the value entered by user is unique.
    :param id_value: The user input to be validated
    :param csv_file_name: The name of the csv file
    :return: Boolean to validate the value
    """
    try:
        with open(f"../../data/{csv_file_name}", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)

            for row in reader:
                if id_value in row:
                    return False
            return True

    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{csv_file_name}' could be not found.")

def booking_id_validator(booking_id):
    """
    Checks if the characters consists of two letters and two digits
    :param booking_id:
    :return:
    """
    booking_id = str(booking_id)
    try:
        if booking_id[:3].isalpha() and booking_id[-2:].isdigit():
            return True
        raise False
    except ValueError:
        raise ValueError(f"Invalid booking id: '{booking_id}'")