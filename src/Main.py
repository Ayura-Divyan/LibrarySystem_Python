import csv

books = {} #Initialised a books dictionary to store the loaded book data

def load_book():
    """Used to load the csv files into python memory"""
    try:
        with open('../data/book.csv', encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile) #Loads the csv file into a variable

            next(reader) #Skips the header row

            for row in reader:
                #Initialise the rows to separate indexes
                if len(row) == 6:
                    book_id = row[0]
                    isbn = row[1]
                    title = row[2]
                    copies = row[3]
                    availability = row[4]
                    price = row[5]

                    #Initialise dictionary
                    books[book_id] = {"title": title, "isbn": isbn, "copies": int(copies), "availability": availability, "price": float(price)}

            print("Books loaded")
    except FileNotFoundError: #Catch
        print("Books file not found")

#Start script
if __name__ == "__main__":
    load_book()

    print(books)