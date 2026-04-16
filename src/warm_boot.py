import csv
import os

DATA_DIR = '../data/'

import csv
import os

DATA_DIR = '../data/'


def load_csv_data(filename, primary_field, fieldnames):
    """
    Loads the data from the csv file
    :param filename:
    :param primary_field:
    :param fieldnames:
    :return:
    """
    data_dict = {}
    filepath = os.path.join(DATA_DIR, filename)

    # Check if the file doesn't exist OR is completely empty (0 bytes)
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        print(f"Warning: {filename} is empty or missing. Initializing blank database.")
        try:
            with open(filepath, mode="w", encoding="utf-8", newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
            return {}  # Return an empty dictionary to the main program
        except Exception as e:
            print(f"Error initializing {filename}: {e}")
            return {}

    try:
        with open(filepath, mode="r", encoding="utf-8", newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            expected_columns = len(fieldnames)

            for row_idx, row in enumerate(reader, start=2):
                if len(row) != expected_columns:
                    print(f"Skipping line {row_idx} in {filename}: Incorrect column count.")
                    continue

                item_id = row.pop(primary_field)
                data_dict[item_id] = row

            print(f"Loaded {len(data_dict)} items from {filename}.")
            return data_dict

    except Exception as e:
        print(f"An unexpected error occurred loading {filename}: {e}")
        return {}



def save_csv_data(filename, data_dict, primary_field):
    """
    Saves data into CSV file
    :param filename:
    :param data_dict:
    :return:
    """
    filepath = os.path.join(DATA_DIR, filename)

    # Handles if there is no data in the dictionary
    if not data_dict:
        print(f"Error: No data to save for {filename}")
        return

    # Getting the headers
    first_element_id = next(iter(data_dict))
    fieldnames = [primary_field] + list(data_dict[first_element_id].keys())

    # Write file
    try:
        with open(filepath, mode="w", newline='') as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            csv_writer.writeheader() # Writes header row

            for item_id, details in data_dict.items():
                row = details.copy() # Creates copy of details to prevent data in memory to be changed
                row[primary_field] = item_id
                csv_writer.writerow(row)
            print(f"Saved {len(data_dict)} items to {filename}.")
    except Exception as e:
        print(f"An unexpected error occurred saving {filename}: {e}")