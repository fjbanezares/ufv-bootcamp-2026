# Example 1: Singleton Nature of None
print("Example 1: Singleton Nature of None")
a = None
b = None

# 'id()' returns the unique identifier for an object, which is its memory address.
# Since 'None' is a singleton, both 'a' and 'b' will have the same 'id'.
print(f"a is b: {a is b}")  # True, because both 'a' and 'b' reference the same None object
print(f"id(a): {id(a)}, id(b): {id(b)}")  # Both will have the same ID (memory address)

# Example 2: Type Checking
print("\nExample 2: Type Checking")
# 'type()' returns the type of the given object.
# For 'None', it will return '<class 'NoneType'>', indicating its unique type.
print(f"type(None): {type(None)}")  # <class 'NoneType'>

# Example 3: Comparisons with None
print("\nExample 3: Comparisons with None")
x = None
# Using 'is' for comparison is recommended because it checks identity, not equality.
# It ensures that 'x' is exactly 'None' and not just an object that equals 'None'.
if x is None:
    print("x is None")  # This will print

# Using '==' for comparison is not recommended because it can be overridden by custom classes.
class CustomNone:
    def __eq__(self, other):
        return True   # overridden to always return 'True'.

y = CustomNone()
# This will print 'True' because the '==', or 'eq', method is overridden to always return 'True'.
print(f"y == None: {y == None}")  # True
# This will print 'False' because 'is' checks identity, and 'y' is not 'None'.
print(f"y is None: {y is None}")  # False

# Example 4: Function Returns
print("\nExample 4: Function Returns")
def no_return():
    pass  # This function doesn't return anything explicitly

def explicit_none_return():
    return None  # This function explicitly returns 'None'

# Functions without a return statement return 'None' by default.
print(f"no_return() returns: {no_return()}")  # None
print(f"explicit_none_return() returns: {explicit_none_return()}")  # None

# Example 5: Using None as Default Argument
print("\nExample 5: Using None as Default Argument")
def append_to_list(value, my_list=None):
    # If 'my_list' is 'None', we create a new list to avoid shared mutable default arguments.
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list

# First call with 'None' as the default for 'my_list'
result = append_to_list(1)
print(f"First call result: {result}")  # [1]
# Second call with 'None' as the default for 'my_list'
result = append_to_list(2)
print(f"Second call result: {result}")  # [2]

# Example 6: Sentinel Value
print("\nExample 6: Sentinel Value")
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

# Creating a simple linked list where 'None' is used to indicate the end of the list.
node1 = Node(1)
node2 = Node(2, node1)
node3 = Node(3, node2)

# Traversing the linked list until we reach 'None'
current_node = node3
while current_node is not None:
    print(f"Node data: {current_node.data}")
    current_node = current_node.next_node

# Example 7: Placeholder for Future Implementation
print("\nExample 7: Placeholder for Future Implementation")
def future_function():
    # Placeholder implementation: This function does nothing for now.
    pass

# Calling a function that currently does nothing and returns 'None'
print(f"future_function() returns: {future_function()}")  # None
