# Import the 'os' module to use operating system-dependent functionality.
import os

# Import the 'logo' variable from the 'art' module.
# This logo will be displayed at the beginning of the calculator program.
from art import logo

# Define a function to clear the console.


def clear_console():
    """
    Clears the console using system-specific commands.
    """
    system = os.name
    if system == "posix":
        # For UNIX systems (Linux/Mac)
        os.system("clear")
    elif system == "nt":
        # For Windows systems
        os.system("cls")

# Define the 'add' function that takes two parameters and returns their sum.


def add(n1, n2):
    return n1 + n2

# Define the 'subtract' function that takes two parameters and returns their difference.


def subtract(n1, n2):
    return n1 - n2

# Define the 'multiply' function that takes two parameters and returns their product.


def multiply(n1, n2):
    return n1 * n2

# Define the 'divide' function that takes two parameters and returns their quotient.


def divide(n1, n2):
    return n1 / n2


# Define a dictionary named 'operations' where:
# - The keys are strings representing arithmetic operators.
# - The values are the functions defined above that perform the corresponding operations.
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Define the main function 'calculator' that drives the calculator program.


def calculator():
    # Display the 'logo' at the beginning of the program.
    print(logo)

    # Prompt the user for the first number and convert the input to a float.
    num1 = float(input("What's the first number?: "))

    # Display all available operation symbols to the user.
    for symbol in operations:
        print(symbol)

    # This flag will determine if the calculator should continue running.
    should_continue = True

    # Main loop of the calculator.
    while should_continue:
        # Prompt the user to pick an arithmetic operation.
        operation_symbol = input("Pick an operation: ")

        # Prompt the user for the second number and convert the input to a float.
        num2 = float(input("What's the next number?: "))

        # Retrieve the appropriate function from the 'operations' dictionary using the chosen operation symbol.
        calculation_function = operations[operation_symbol]

        # Call the retrieved function with 'num1' and 'num2' as arguments and store the result in 'answer'.
        answer = calculation_function(num1, num2)

        # Display the calculation and the result to the user.
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # Ask the user if they want to continue with the current result or start a new calculation.
        user_input = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        # If the user chooses to continue, update 'num1' with the current 'answer'.
        if user_input == 'y':
            num1 = answer
        else:
            should_continue = False
            clear_console()
            calculator()


# Call the 'calculator' function to start the program.
calculator()
