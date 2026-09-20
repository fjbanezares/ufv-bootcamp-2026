# naming_conventions_example.py

# Please note: This script demonstrates Python's naming conventions for variables, constants, classes, functions, and methods.
# Naming conventions help keep code readable and understandable. Thank you for following along!

# Example 1: Variable Naming Conventions

# Variables in Python typically use snake_case (all lowercase with underscores).
user_name = "Alice"
print(f"The variable 'user_name' holds the value: {user_name}")

# Please understand: Using snake_case for variable names makes the code more readable and consistent with Python's style guidelines.

# Example 2: Constant Naming Conventions

# Constants use UPPER_CASE_WITH_UNDERSCORES.
PI = 3.14159
MAX_SIZE = 100

print(f"The constant 'PI' holds the value: {PI}")
print(f"The constant 'MAX_SIZE' holds the value: {MAX_SIZE}")

# Please note: Constants are variables that should not change after they are initialized.
# Although Python does not enforce immutability, using uppercase with underscores indicates that these values should remain constant.

# Example 3: Class Naming Conventions

# Classes use CamelCase (initial uppercase letter for each word, no underscores).
class UserProfile:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Example 4: Method Naming Conventions

    # Methods (and functions) use snake_case.
    def calculate_age_in_years(self, current_year):
        return current_year - self.age

    # Example of a "dunder" (double underscore) method
    def __str__(self):
        return f"UserProfile(name={self.name}, age={self.age})"

# Creating an instance of the UserProfile class
user = UserProfile("Alice", 30)
print(user)

# Thank you for noticing: Classes use CamelCase to distinguish class names from variable and function names, which enhances readability.

# Example 5: Protected and Private Variable Naming Conventions

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public variable
        self._protected_balance = balance     # Protected variable (single underscore)
        self.__private_key = "secret_key"     # Private variable (double underscore)

    def display_balance(self):
        print(f"{self.account_holder} has a balance of: {self._protected_balance}")

    # Example of accessing a private variable using a public method
    def get_private_key(self):
        return self.__private_key

# Creating an instance of the BankAccount class
account = BankAccount("John Doe", 1500)

# Accessing public and protected variables
print(f"Account Holder: {account.account_holder}")
print(f"Protected Balance: {account._protected_balance}")  # Not recommended to access directly

# Attempting to access a private variable will cause an AttributeError
try:
    print(account.__private_key)
except AttributeError:
    print("Cannot access private variable directly!")

# Accessing private variable using a public method
print(f"Accessing private variable through method: {account.get_private_key()}")

# Thank you for your patience: Protected and private naming conventions are used to indicate how variables should be accessed.
# Protected variables are intended for use within the class or subclass, while private variables are meant strictly for internal use within the class.

# Summary:
# - **Snake_case**: Used for variable and function/method names to improve readability.
# - **UPPER_CASE_WITH_UNDERSCORES**: Used for constants to indicate they should not change.
# - **CamelCase**: Used for class names to differentiate them from variables and functions.
# - **Single leading underscore (_)**: Indicates a protected variable, suggesting it's for internal use.
# - **Double leading underscore (__)**: Indicates a private variable, meant to be used only within the class where it's defined.
# - **Dunder (double underscore) methods**: Special methods with double underscores before and after, like `__init__` and `__str__`.

# Thank you for exploring these naming conventions with us! Please continue to practice these conventions in your Python code to make it more readable and maintainable.
