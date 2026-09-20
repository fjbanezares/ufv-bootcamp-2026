# Leap Year and Days in Month Challenge

# This function should determine if a given year is a leap year.
# Modify it to return True or False instead of printing the results.
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year.")
            else:
                print("Not leap year.")
        else:
            print("Leap year.")
    else:
        print("Not leap year.")

# This function should determine the number of days in a given month for a specific year.
# Use the provided month_days list and the is_leap function to achieve this.
# Remember, month_days is zero-indexed, so January is month_days[0].


def days_in_month():
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # TODO: Your code here


# Do NOT modify the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
