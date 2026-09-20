"""
This script demonstrates how to overload the + operator in Python by extending 
the behavior of the int class. We will create a custom class called CustomInt 
that allows the following:

1. Add an integer and a string (e.g., 5 + "5" should return 10).
2. Add an integer and a list (e.g., 5 + [1, 2, 3] should return [6, 7, 8]).
3. Add two integers normally (e.g., 5 + 3 should return 8).

Additionally, we will also implement a simple function called custom_add() that 
performs similar operations for comparison.
"""

# Custom class that extends the behavior of the built-in int type
class CustomInt(int):
    # Overloading the + operator with __add__ method
    def __add__(self, other):
        """
        The __add__ method is called when we use the + operator with a CustomInt 
        object. This method will handle different types for the second operand (other).
        """
        # If the second operand (other) is a string, convert it to an integer
        if isinstance(other, str):
            # Convert both self (the integer) and other (the string) to integers
            return int(self) + int(other)
        
        # If the second operand is a list, add the integer to each element in the list
        elif isinstance(other, list):
            # Create a new list with each element being the sum of self and each item in the list
            return [int(self) + int(item) for item in other]
        
        # For any other type, fall back to normal integer addition
        return int(self) + other

# Now, let's test the CustomInt class with different cases
# Example 1: Adding an integer and a string
a = CustomInt(5)
print(a + "5")  # Should output 10 because "5" will be converted to an integer

# Example 2: Adding an integer and a list
print(a + [1, 2, 3])  # Should output [6, 7, 8] because 5 will be added to each element

# Example 3: Adding two integers
print(a + 3)  # Should output 8 because it's a normal integer addition

###############################################################################

# Now let's implement a function that does similar work without overloading the operator
def custom_add(a, b):
    """
    This function adds two values (a and b) with special handling:
    - If b is a string, convert it to an integer and then add it to a.
    - If b is a list, add a to each element in the list.
    - For any other types, return their sum.
    """
    # If the second operand is a string, convert it to an integer
    if isinstance(a, int) and isinstance(b, str):
        return a + int(b)
    
    # If the second operand is a list, add a to each element in the list
    elif isinstance(a, int) and isinstance(b, list):
        return [a + int(item) for item in b]
    
    # For any other case, just return the result of adding a and b
    return a + b

# Let's test the function with the same cases as before
# Example 1: Adding an integer and a string
print(custom_add(5, "5"))  # Should output 10

# Example 2: Adding an integer and a list
print(custom_add(5, [1, 2, 3]))  # Should output [6, 7, 8]

# Example 3: Adding two integers
print(custom_add(5, 3))  # Should output 8

"""
To summarize:
- We extended the int class to handle custom addition with strings and lists using operator overloading (__add__).
- We also implemented a separate function, custom_add(), for those who prefer not to modify the behavior of the + operator.
Both approaches are valid, and the choice depends on your use case!
"""

