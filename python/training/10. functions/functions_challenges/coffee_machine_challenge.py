# Your task is to complete the coffee machine program.
# Some parts are missing, so you will need to figure out how to complete it.
# Make sure to read the comments for hints!

# The MENU dictionary is already complete. It contains the drinks, their ingredients, and costs.
MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
}

# TODO: Initialize a 'profit' variable to 0.

# The resources in the coffee machine are pre-defined.
resources = {"water": 300, "milk": 200, "coffee": 100}

# TODO: Complete the function that checks if resources are sufficient to make a drink.


def is_resource_sufficient(order_ingredients):
    pass  # Your code goes here

# TODO: Complete the function that processes coins and returns the total.


def process_coins():
    pass  # Your code goes here

# TODO: Complete the function that handles the transaction.


def is_transaction_successful(money_received, drink_cost):
    pass  # Your code goes here

# TODO: Complete the function to make the coffee and update resources.


def make_coffee(drink_name, order_ingredients):
    pass  # Your code goes here

# TODO: Initialize a variable to control the coffee machine loop.


# Main program loop. You shouldn't need to modify this.
while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        # TODO: Implement a feature to print the current resources and profit.
    else:
        # TODO: Implement the workflow to handle a drink choice,
        # check resources, process payment, and make coffee.
