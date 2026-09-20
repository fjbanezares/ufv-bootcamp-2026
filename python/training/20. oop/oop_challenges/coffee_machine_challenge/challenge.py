# Coffee Machine Challenge

"""
Your challenge is to refactor this single .py file into three separate Python files:
1. menu.py: Should contain the Menu and MenuItem classes.
2. coffee_maker.py: Should contain the CoffeeMaker class.
3. money_machine.py: Should contain the MoneyMachine class.

Once you separate these into their respective files, you'll need to import them back into this main file.
"""

# ----- Menu Class and Menu Item Class -----
# Hints: Create a separate file called 'menu.py' and place these classes inside it.

class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
        }

class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            # TODO: Add more menu items
        ]
    def get_items(self):
        # TODO: Return the names of menu items.
        pass
    def find_drink(self, order_name):
        # TODO: Return a MenuItem object if it exists, else None
        pass

# ----- Coffee Maker -----
# Hints: Create a separate file called 'coffee_maker.py' and place this class inside it.

class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
    def report(self):
        # TODO: Print the current resource levels

# TODO: Implement more methods to handle resources and coffee making.

# ----- Money Machine -----
# Hints: Create a separate file called 'money_machine.py' and place this class inside it.

class MoneyMachine:
    def __init__(self):
        self.profit = 0
        # TODO: Add more initialization code if needed

    def report(self):
        # TODO: Print current money status

# TODO: Implement methods to process coins and handle payments.

# ------ Main Program ------
# Hints: After creating separate files and classes, import them back here.
# Uncomment the following import statements after you create the corresponding classes.

# from menu import Menu, MenuItem
# from coffee_maker import CoffeeMaker
# from money_machine import MoneyMachine

if __name__ == "__main__":
    # Initialize Menu and MenuItem objects
    menu = Menu()
    
    # Initialize CoffeeMaker
    coffee_maker = CoffeeMaker()
    
    # Initialize MoneyMachine
    money_machine = MoneyMachine()
    
    is_on = True
    while is_on:
        options = menu.get_items()
        choice = input(f"What would you like? ({options}): ")
        # TODO: Take the user's choice and implement functionality for 'off', 'report', and making coffee.
