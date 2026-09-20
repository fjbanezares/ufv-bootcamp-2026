# Define a CoffeeMaker class
class CoffeeMaker:
    """
    Models the machine that makes the coffee.

    Attributes:
    - resources (dict): A dictionary containing the available resources
                        to make coffee drinks.
    """

    # Initialize the CoffeeMaker object with default resources
    def __init__(self):
        """Initialize the coffee maker with available resources."""
        self.resources = {
            "water": 300,  # ml of water
            "milk": 200,  # ml of milk
            "coffee": 100,  # g of coffee
        }

    # Define a report method to print out the current resources
    def report(self):
        """
        Prints a report of all available resources.

        The function goes through each item in the resources dictionary
        and prints its available quantity.
        """
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    # Check if resources are sufficient to make the requested drink
    def is_resource_sufficient(self, drink):
        """
        Returns True when the order can be made, False if ingredients are insufficient.

        Args:
        - drink (object): The drink object containing the required ingredients.

        The function iterates through the ingredients required for the drink
        and compares them against the available resources.
        """
        can_make = True  # Initialize flag as True
        for item in drink.ingredients:
            # Check if each required ingredient is available
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = (
                    False  # Update flag to False if any ingredient is insufficient
                )
        return can_make

    # Deduct the ingredients from the resources to make the coffee
    def make_coffee(self, order):
        """
        Deducts the required ingredients from the resources to make the coffee.

        Args:
        - order (object): The drink object containing the required ingredients.

        The function goes through each ingredient in the order
        and deducts it from the available resources.
        """
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[
                item
            ]  # Deduct the required amount of each ingredient
        print(
            f"Here is your {order.name} ☕️. Enjoy!"
        )  # Notify the user that their coffee is ready
