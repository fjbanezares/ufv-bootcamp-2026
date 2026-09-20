# Importing this module displays the Zen of Python. Please try it!
import this

# Example 1: Beautiful is better than ugly.
# Please note: We aim to write code that is not just functional but also aesthetically pleasing.

# Ugly code example
def calculate_discount(price, rate):
  return price * rate

# Beautiful code example
def calculate_discount(price, discount_rate):
    """
    Calculate the discounted price.

    Parameters:
    price (float): Original price of the item
    discount_rate (float): Discount rate as a decimal

    Returns:
    float: Discounted price
    """
    return price * discount_rate

print("Beautiful is better than ugly, thank you for writing beautiful code!")

# Example 2: Explicit is better than implicit.
# Please be clear in your intentions, so everyone can understand your code.

# Implicit code example
x = [2, 3, 5, 7]
print(sum(x))

# Explicit code example
numbers = [2, 3, 5, 7]  # Please use descriptive names for clarity
total_sum = sum(numbers)
print(total_sum)

print("Explicit is better than implicit, thank you for making your code clear!")

# Example 3: Simple is better than complex.
# Please choose simple solutions when possible.

# Complex code example
def find_even_numbers(numbers):
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens

# Simple code example
def find_even_numbers(numbers):
    """Return a list of even numbers."""
    return [number for number in numbers if number % 2 == 0]

print(find_even_numbers([1, 2, 3, 4, 5, 6]))  # [2, 4, 6]

print("Simple is better than complex, thank you for keeping it simple!")

# Example 4: There should be one-- and preferably only one --obvious way to do it.
# Please follow the obvious way to avoid confusion.

# Non-obvious code example
def get_greeting():
    return "Hello" if True else None

# Obvious code example
def get_greeting():
    return "Hello"

print(get_greeting())  # "Hello"

print("One obvious way is better, thank you for following the clear path!")

# Please remember: The Zen of Python encourages us to write code that is not only functional but also elegant,
# easy to understand, and maintain. By adhering to these principles, we can create code that others will
# appreciate and enjoy reading, making our work more impactful and collaborative. Thank you for embracing Pythonic philosophy!
