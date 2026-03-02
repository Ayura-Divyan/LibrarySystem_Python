#This module is used to validate the input data for a transaction
from datetime import datetime

def date_validator(date):
    """
    Validate the date given to DD/MM/YYYY
    :param date:
    :return:
    """
    try:
        datetime.strptime(date, '%d/%m/%Y')
        return True
    except ValueError:
        return False