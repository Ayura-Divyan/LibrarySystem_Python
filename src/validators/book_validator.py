def isbn_valid(value):
    """
    Validates ISBN number according to International isbn
    :param value:
    :return:
    """
    value = str(value.replace("-", ""))
    if len(value) == 13 and value.isdigit() and (value[:3] in ["978", "979"]):
        return True
    return False