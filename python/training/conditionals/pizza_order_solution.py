# Welcome message for the user to the pizza ordering system.
print("Welcome to Python Pizza Deliveries!")

# Prompt the user to input their desired pizza size (S, M, or L).
size = input("What size pizza do you want? S, M, or L ")

# Initialize the bill to 0.
bill = 0

# Based on the user's choice, set the base price of the pizza.
# Small Pizza: $15, Medium Pizza: $20, Large Pizza: $25
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

# Ask if the user wants to add pepperoni to their pizza.
add_pepperoni = input("Do you want pepperoni? Y or N ")

# Determine the cost of adding pepperoni based on the pizza size.
# For a small pizza, pepperoni costs an additional $2.
# For medium and large pizzas, it's an additional $3.
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# Ask if the user wants extra cheese on their pizza.
extra_cheese = input("Do you want extra cheese? Y or N ")

# If they want extra cheese, add $1 to the bill.
# This cost is the same regardless of pizza size.
if extra_cheese == "Y":
    bill += 1

# Display the final bill to the user.
print(f"Your final bill is: ${bill}.")
