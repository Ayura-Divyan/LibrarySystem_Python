#This module is used to validate the input data for a student

def name(first_name):
    if first_name.isalpha() and len(first_name) <= 10:
        return True
    else:
        return False