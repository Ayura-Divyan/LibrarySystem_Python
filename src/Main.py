import csv

books = {} #Initialised a books dictionary to store the loaded book data

def load_book():
    """Used to load the csv files into python memory"""
    try:
        with open('/data/book.csv') as csvfile:
            reader = csv.reader(csvfile) #Loads the csv file into a variable

            for row in reader:
                if len(row) == 6:
