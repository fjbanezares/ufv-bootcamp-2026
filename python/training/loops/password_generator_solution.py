# Password Generator Project
import random

# Lists of possible characters for our password.
# We have three categories: letters, numbers, and symbols.

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Prompting user for preferences about the password.
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Initializing an empty list to store the characters of the generated password.
password_list = []

# For the specified number of letters, pick a random letter and add it to our password list.
for char in range(nr_letters):
    password_list.append(random.choice(letters))

# For the specified number of symbols, pick a random symbol and add it to our password list.
for char in range(nr_symbols):
    password_list.append(random.choice(symbols))

# For the specified number of numbers, pick a random number and add it to our password list.
for char in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Shuffling the characters to ensure randomness in the final password.
random.shuffle(password_list)

# Constructing the final password string from the shuffled list of characters.
password = "".join(password_list)

# Displaying the generated password to the user.
print(f"Your password is: {password}")
