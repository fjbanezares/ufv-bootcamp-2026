# Define the MenuItem class
class MenuItem:
    """
    Models each menu item for a coffee machine.

    Attributes:
    - name (str): The name of the drink.
    - cost (float): The cost of the drink.
    - ingredients (dict): The ingredients needed to make the drink.
    """

    def __init__(self, name, water, milk, coffee, cost):
        """
        Initializes a MenuItem object with a name, water, milk, coffee, and cost.

        Args:
        - name (str): The name of the drink.
        - water (int): The amount of water needed in milliliters.
        - milk (int): The amount of milk needed in milliliters.
        - coffee (int): The amount of coffee needed in grams.
        - cost (float): The cost of the drink.
        """
        self.name = name
        self.cost = cost
        self.ingredients = {"water": water, "milk": milk, "coffee": coffee}


# Define the Menu class
class Menu:
    """
    Models the entire menu containing a list of MenuItem objects.

    Attributes:
    - menu (list): A list containing MenuItem objects for each available drink.
    """

    def __init__(self):
        """
        Initializes a Menu object with a list of MenuItem objects.

        The list contains pre-defined MenuItem objects with name, cost, and ingredients.
        """
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """
        Returns a string containing the names of all the menu items, separated by slashes.

        This function iterates over the menu items and concatenates their names into a single string.
        """
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """
        Searches the menu for a particular drink by its name and returns the MenuItem object if found.

        Args:
        - order_name (str): The name of the drink to search for.

        Returns:
        - MenuItem object if found, otherwise prints an error message and returns None.
        """
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
