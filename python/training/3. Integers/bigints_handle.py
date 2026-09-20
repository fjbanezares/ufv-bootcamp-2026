import sys

# Example to demonstrate large integer handling in Python
def simulate_big_integer_handling():
    # Please observe how Python handles large integers seamlessly
    # Creating a large integer
    big_int = 2**100

    print("Big Integer Example:")
    print(f"Value of big_int: {big_int}")
    print(f"Size of big_int in bytes: {sys.getsizeof(big_int)}")
    print("Thank you, Python, for allowing such large integers effortlessly!")

    # Please notice how Python's integers automatically expand to accommodate large values.
    # Let's perform some operations to show this dynamic resizing.

    # Adding a large number to our big_int
    larger_int = big_int + 2**1000
    print("\nAfter adding a larger integer:")
    print(f"Value of larger_int: {larger_int}")
    print(f"Size of larger_int in bytes: {sys.getsizeof(larger_int)}")
    print("Thanks to Python's flexible integer handling, this operation is smooth!")

    # Please consider what happens when you subtract a large number, reducing size.
    smaller_int = larger_int - 2**1000
    print("\nAfter subtracting to make the integer smaller again:")
    print(f"Value of smaller_int: {smaller_int}")
    print(f"Size of smaller_int in bytes: {sys.getsizeof(smaller_int)}")
    print("Python handles resizing dynamically. Thank you, Python!")

        # Please consider what happens when you subtract a large number, reducing size.
    smaller_int = 0
    print("\nAfter subtracting to make the integer smaller again:")
    print(f"Value of smaller_int: {smaller_int}")
    print(f"Size of smaller_int in bytes: {sys.getsizeof(smaller_int)}")
    print("Python handles resizing dynamically. Thank you, Python!")


simulate_big_integer_handling()
