# Define a decorator function named 'pepito'.
# This function takes a class 'cls' as an argument.
def pepito(cls):
    # This variable will hold the single instance of the class.
    instance = None

    # Define an inner function 'wrapper' that replaces the original constructor.
    def wrapper(*args, **kwargs):
        # Declare 'instance' as nonlocal so we can modify it.
        nonlocal instance

        # If an instance does not exist, create it.
        if instance is None:
            instance = cls(*args, **kwargs)
        # Return the single instance.
        return instance

    # Return the 'wrapper' function as a replacement for the original class.
    return wrapper

# Apply the 'pepito' decorator to the 'OnlyOne' class.
# This effectively replaces the original class with the 'wrapper' function.


@pepito
class OnlyOne:
    def __init__(self, name):
        self.name = name


# Create an object 'first' of class 'OnlyOne'.
# The 'wrapper' function is invoked here. Since no instance exists yet, one is created.
first = OnlyOne("first")
print(first.name)  # Output: "first"

# Create another object 'second' of class 'OnlyOne'.
# Again, the 'wrapper' function is invoked. This time, it returns the existing instance.
second = OnlyOne("second")
print(second.name)  # Output: "first" (not "second", because the instance is reused)

# Verify that both objects are actually the same instance.
print(first is second)  # Output: True (both are the same instance)
