def isbn_valid(value):
    """
    Validates ISBN number according to International ISBN Standard.
    :param value:
    :return:
    """
    digits = str(value).replace("-", "").replace(" ", "") #Cleaning out the isbn

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
    if len(title) > 20 and not title.isalpha(): #Title has to contain only letters with a max length of 20
        return False
    else:
        return True