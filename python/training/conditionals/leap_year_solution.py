# We start by taking the user's input for the year they'd like to check.
year = int(input("Which year do you want to check? "))

# The conditions for a leap year are:
# 1. The year should be divisible by 4.
# 2. If the year is divisible by 100, it should also be divisible by 400 to be a leap year.

# Let's start by checking if the year is divisible by 4.
if year % 4 == 0:
    # If the year is divisible by 100, we check for divisibility by 400.
    if year % 100 == 0:
        # If it's also divisible by 400, it's a leap year.
        if year % 400 == 0:
            print("Leap year.")
        # If not divisible by 400, then it's not a leap year.
        else:
            print("Not leap year.")
    # If the year is divisible by 4 but not by 100, then it's a leap year.
    else:
        print("Leap year.")
# If the year is not divisible by 4 at all, it's not a leap year.
else:
    print("Not leap year.")
