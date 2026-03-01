import csv

def is_unique(value, csv_file_name):
    """
    Checks if the value entered by user is unique.
    :param value: The user input to be validated
    :param csv_file_name: The name of the csv file
    :return:
    """
    try:
        with open(f"../../data/{csv_file_name}", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)

            for row in reader:
                if value in row:
                    return False
            return True

    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{csv_file_name}' could be not found.")