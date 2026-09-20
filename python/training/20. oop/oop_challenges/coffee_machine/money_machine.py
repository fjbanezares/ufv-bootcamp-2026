# Define a MoneyMachine class
class MoneyMachine:
    """
    Handles all the money transactions within the coffee machine.

    Class Attributes:
    - CURRENCY (str): The currency symbol used for all transactions.
    - COIN_VALUES (dict): A dictionary containing the value of different types of coins.
    """

    # Class constants for currency symbol and coin values
    CURRENCY = "$"
    COIN_VALUES = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}

    # Initialize the MoneyMachine object
    def __init__(self):
        """
        Initializes the MoneyMachine with a profit of 0 and a money_received of 0.

        Attributes:
        - profit (float): The total money made by the machine.
        - money_received (float): The total money received in the current transaction.
        """
        self.profit = 0
        self.money_received = 0

    # Report the current profit
    def report(self):
        """
        Prints the current profit in the machine.

        The function simply prints out the total profit accumulated so far.
        """
        print(f"Money: {self.CURRENCY}{self.profit}")

    # Process the coins inserted by the user
    def process_coins(self):
        """
        Returns the total money calculated from coins inserted.

        This function asks the user to insert different types of coins
        and adds up their value.
        """
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += (
                int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
            )
        return self.money_received

    # Handle payment logic
    def make_payment(self, cost):
        """
        Returns True when payment is accepted, or False if the money is insufficient.

        Args:
        - cost (float): The cost of the item to be purchased.

        This function first processes the inserted coins and then checks if the
        user has inserted enough money for the item.
        """
        self.process_coins()  # First, process all the coins inserted by the user

        # Check if inserted money is sufficient
        if self.money_received >= cost:
            # Calculate and display the change
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")

            # Update the profit
            self.profit += cost

            # Reset the money received for the next transaction
            self.money_received = 0

            return True  # Payment was successful
        else:
            # Inform the user that the money was insufficient
            print("Sorry that's not enough money. Money refunded.")

            # Reset the money received for the next transaction
            self.money_received = 0

            return False  # Payment failed
