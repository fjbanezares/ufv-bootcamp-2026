# Password Generator Challenge
# Your task is to generate a strong random password based on user preferences.
# Some parts of the code have been removed. You need to fill them in!
# Use the hints provided in comments and the knowledge you've gained so far.

import random

letters = [ ... ]  # Fill in the list of letters
numbers = [ ... ]  # Fill in the list of numbers
symbols = [ ... ]  # Fill in the list of symbols

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

# Write a loop to add random letters to password_list based on nr_letters
# HINT: Use random.choice() to pick a random item from a list

# Write a loop to add random symbols to password_list based on nr_symbols

# Write a loop to add random numbers to password_list based on nr_numbers

# Shuffle the password_list

# Construct the final password from the shuffled list and display it to the user.
# HINT: You can use the join() method to convert a list into a string.
