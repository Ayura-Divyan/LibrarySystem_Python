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
                    return False #If the id already exists in the csv file it will raise the error return false
    except FileNotFoundError:
        print(f"Error: File '{csv_file_name}' could be not found.")

def booking_id_validator(booking_id):
    """
    Checks if the characters consists of two letters, two digits and the length is four digits.
    :param booking_id:
    :return:
    """
    booking_id = str(booking_id)
    if len(booking_id) == 4 and booking_id[:2].isalpha() and booking_id[-2:].isdigit():
        return True
    else:
       return False #If the id doesn't meet the validation it return False

def student_id_validator(student_id):
    """
    Checks if the student id is eight digits.
    :param student_id:
    :return:
    """
    student_id = str(student_id) #Convert to string so that it can be parsed for the len and .isdigit

    if student_id.isdigit() and len(student_id) == 8:
        return True
    else:
        return False