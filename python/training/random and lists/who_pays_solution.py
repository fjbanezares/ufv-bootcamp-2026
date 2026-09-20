# To utilize randomness in our program, we need to import the random module.
import random

# Get all names from the user.
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# Calculate the number of names in the list.
number_of_names = len(names)

# Generate a random number between 0 and the last index of the list.
random_index = random.randint(0, number_of_names - 1)

# Select the name that corresponds to the random index.
person_who_will_pay = names[random_index]

print(f"{person_who_will_pay} is going to buy the meal today!")
