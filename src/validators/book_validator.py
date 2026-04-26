#This module is used to validate the input data for a book

def isbn_valid(isbn):
    """
    Validates ISBN according to International ISBN Standard.
    :param isbn:
    :return:
    """
    digits = str(isbn).replace("-", "").replace(" ", "") #Cleaning out the isbn

    if len(digits) != 13 or not digits.isdigit():
        return False

    if digits[:3] not in ["978", "979"]:
        return False

    #Checksum calculation
    total = 0
    for i, digit in enumerate(digits):
        if i % 2 == 0:
            total += int(digit) * 1
        else:
            total += int(digit) * 3

    return total % 10 == 0

def title_valid(title):
    """
    Validates the book title
    :param title:
    :return:
    """
    title = title.replace(" ", "")
    if len(title) > 20 or not title.isalpha(): #Title has to contain only letters with a max length of 20
        return False
    else:
        return True

def copy_valid(copies):
    """
    Validates the number of copies of a book
    :param copies:
    :return:
    """
    copies = str(copies)

    if copies.isdigit() and (2 >= int(copies) >= 0):
        return True
    else:
        return False

def price_valid(price):
    """
    Validates the price of a book
    :param price:
    :return:
    """
    price = str(price)

    price_parts = price.split(".") #Creates a list that's split at the decimal point

    if len(price_parts) != 2:
        return False

    if price_parts[0].isdigit() and price_parts[1].isdigit() and (len(price_parts[1]) == 2):
        return True
    else:
        return False
