# We start by taking the user's input for the year they'd like to check.
year = int(input("Which year do you want to check? "))

# Using elif allows us to combine conditions and make the code structure clearer.

# First, we'll check the condition where the year is divisible by 100.
# If true, we'll further check if it's divisible by 400.
if year % 100 == 0:
    if year % 400 == 0:
        print("Leap year.")
    else:
        print("Not leap year.")
# If the year isn't divisible by 100, we simply check if it's divisible by 4.
elif year % 4 == 0:
    print("Leap year.")
else:
    print("Not leap year.")
