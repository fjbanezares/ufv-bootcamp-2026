# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# First, we need to convert the input string to an integer.
current_age = int(age)

# The number of years a person has left if they live until 90.
years_left = 90 - current_age

# Now, let's calculate the number of days, weeks, and months left.
# We'll use some approximations for this:
# A year has about 365.25 days on average, accounting for leap years.
# A month is roughly 30.44 days on average.
# A week is 7 days.

days_left = years_left * 365.25  # Using 365.25 to consider the leap year.
weeks_left = years_left * 52  # There are 52 weeks in a year.
months_left = years_left * 12  # There are 12 months in a year.

# Now, let's inform the user about the time they have left, using f-Strings for string formatting.
message = f"You have {int(days_left)} days, {int(weeks_left)} weeks, and {months_left} months left."
print(message)
