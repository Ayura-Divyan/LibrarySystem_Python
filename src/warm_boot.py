import csv
import os

DATA_DIR = '../data/'


def load_csv_data(filename, key_field, expected_columns):
    """
    Loads data from CSV file
    :param filename:
    :param key_field:
    :param expected_columns:
    :return :
    """
    data_dict = {}
    filepath = os.path.join(DATA_DIR, filename)

    try:
        with open(filepath, mode="r", encoding="utf-8", newline='') as csvfile:
            # DictReader uses the first row (header) as keys for each row dictionary
            reader = csv.DictReader(csvfile)

            for row_idx, row in enumerate(reader, start=2):
                if len(row) != expected_columns:
                    print(f"Skipping line {row_idx} in {filename}: Incorrect column count.")
                    continue

                # Extract the ID to use as the dictionary key
                item_id = row.pop(key_field)
                data_dict[item_id] = row
            return data_dict

    except FileNotFoundError:
        print(f"Error: The file {filename} was not found in {DATA_DIR}")
    except Exception as e:
        print(f"An unexpected error occurred loading {filename}: {e}")
    return {}