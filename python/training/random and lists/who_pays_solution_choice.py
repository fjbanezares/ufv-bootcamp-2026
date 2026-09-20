# To utilize randomness in our program, we need to import the random module.
import random

# Get all names from the user.
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# Directly choose a random name from the list using the choice() function.
person_who_will_pay = random.choice(names)

print(f"{person_who_will_pay} is going to buy the meal today!")
