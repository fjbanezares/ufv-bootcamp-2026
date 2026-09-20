# Import the necessary classes from the other Python modules
# Demonstrating code modularity and reusability.
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Initialize MoneyMachine, CoffeeMaker, and Menu classes.
# Each object is responsible for handling its own domain,
# thereby demonstrating encapsulation and object-oriented design.
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# Declare a boolean variable to control the operation of the coffee machine.
# Essentially serves as the power button for the machine.
is_on = True

# Start of the main program loop, representing the continual operation of the coffee machine
# until it is turned off.
while is_on:
    # Fetch the available menu items and show them to the user.
    # This demonstrates object interaction and message passing.
    options = menu.get_items()

    # Collects user input for their menu choice.
    # This is the point of interaction with an external entity (the user).
    choice = input(f"What would you like? ({options}): ")

    # Check for 'off' command to turn off the coffee machine.
    # Terminates the loop, effectively "turning off" the machine.
    if choice == "off":
        is_on = False

    # Check for 'report' command to display current resource status.
    # Calls the 'report' method from both CoffeeMaker and MoneyMachine classes,
    # showing the current status of resources and money.
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    # For any other user input, attempt to make the coffee.
    else:
        # Search for the drink in the menu.
        # Demonstrates object interaction and conditional checks.
        drink = menu.find_drink(choice)

        # Check if resources are sufficient and if payment is successful to make the coffee.
        # Multiple method calls from different objects are combined in a single line.
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(
            drink.cost
        ):
            # Make the selected coffee.
            # The final step in fulfilling the user's request, showcasing the culmination of
            # all object interactions and method calls.
            coffee_maker.make_coffee(drink)
