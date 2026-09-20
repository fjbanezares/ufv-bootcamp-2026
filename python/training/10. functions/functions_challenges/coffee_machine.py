# MENU is a dictionary that defines the drinks and their properties such as ingredients and cost.
# This acts as the data model for the coffee machine.
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Initialize profit variable to keep track of earnings.
# Profit starts at 0 because no drinks have been sold yet.
profit = 0

# Dictionary to hold the current resources available in the machine.
# These resources will be depleted as drinks are made.
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Function to check if resources are sufficient to make the desired drink.
# Takes the ingredients for a specific drink as an argument.


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        # If any ingredient in the order is more than the available resource, return False.
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    # Return True if all ingredients are sufficient.
    return True

# Function to process the coins inserted by the user.
# Returns the total value of the coins.


def process_coins():
    print("Please insert coins.")
    # Collect different types of coins and calculate their total value.
    # Note: The coin values are hard-coded for simplicity.
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

# Function to check if the transaction was successful.
# Takes the total money received and the cost of the drink as arguments.


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit  # Use the global profit variable to update it.
        # Update the profit by adding the cost of the drink.
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

# Function to make the coffee and update the resources.
# Takes the name of the drink and its ingredients as arguments.


def make_coffee(drink_name, order_ingredients):
    # Loop through the ingredients and deduct them from the available resources.
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


# Initialize a variable to control the while loop for the coffee machine.
is_on = True

# Main program loop for the coffee machine.
while is_on:
    # Ask the user for their drink choice.
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    # Secret command to turn off the machine.
    if choice == "off":
        is_on = False
    # Report command to check the current resources and profit.
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    # When a drink type is chosen.
    else:
        drink = MENU[choice]  # Get the drink details from the MENU dictionary.
        # Check if there are sufficient resources to make the drink.
        if is_resource_sufficient(drink["ingredients"]):
            # Process the coins and get the total money.
            payment = process_coins()
            # Check if the transaction is successful.
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])  # Make the coffee.
