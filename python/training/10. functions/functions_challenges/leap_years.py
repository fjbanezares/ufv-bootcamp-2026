# Leap Year and Days in Month Solution

def is_leap(year):
    """
    Determine if the given year is a leap year.

    A leap year in the Gregorian calendar is defined as a year that:
    1. Is divisible by 4.
    2. Is not divisible by 100, unless it's also divisible by 400.

    This means that years like 2000 and 2400 are leap years because they are divisible by 400,
    but 1800, 1900, 2100 are not, even though they are divisible by 4, because they are divisible by 100 but not by 400.

    Args:
    - year (int): The year to check. Should be a positive integer.

    Returns:
    - bool: True if the year is a leap year, otherwise False.

    Examples:
    >>> is_leap(2000)
    True
    >>> is_leap(2100)
    False
    >>> is_leap(2204)
    True
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    """
    Determine the number of days in a given month of a specific year.

    This function takes into account leap years for February. 
    All other months have a fixed number of days.

    Args:
    - year (int): The year in which the month occurs. Should be a positive integer.
    - month (int): The month number (1 for January, 12 for December). Should be an integer between 1 and 12.

    Returns:
    - int: Number of days in the specified month of the given year.

    Examples:
    >>> days_in_month(2022, 2)
    28
    >>> days_in_month(2000, 2)
    29
    >>> days_in_month(2204, 12)
    31
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2 and is_leap(year):
        return 29
    return month_days[month - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
