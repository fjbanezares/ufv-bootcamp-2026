# Singleton Decorator: Using nonlocal
# --------------------------------------------------------------
# This implementation uses the "nonlocal" keyword to track the 
# instance of the class inside the closure. It ensures that we 
# create only one instance by checking if the "instance" variable 
# is None before creating the object. Thanks for following along!
def singleton_nonlocal(cls):
    instance = None  # Start with no instance (set to None)
    
    # Wrapper function to manage the instance creation
    def wrapper(*args, **kwargs):
        nonlocal instance  # Allows us to modify the outer 'instance' variable
        if instance is None:
            instance = cls(*args, **kwargs)  # Create the instance if it doesn't exist
        return instance  # Return the same instance
    return wrapper  # Return the wrapped function

# Applying the singleton_nonlocal decorator to a class
@singleton_nonlocal
class OnlyOneWithNonlocal:
    def __init__(self, name):
        self.name = name

# Test Singleton behavior with nonlocal
first_instance = OnlyOneWithNonlocal("First")
second_instance = OnlyOneWithNonlocal("Second")

# Both should refer to the same instance, and both will print the name "First"
print(first_instance.name)  # Output: First
print(second_instance.name)  # Output: First
print(first_instance is second_instance)  # Output: True

# --------------------------------------------------------------
# Singleton Decorator: Using a Dictionary
# --------------------------------------------------------------
# This implementation uses a dictionary to track instances of the 
# class. The class itself is used as the key, so it supports multiple 
# singletons for different classes. Thank you for following! This version
# is a bit more flexible, but both have their pros and cons.

def singleton_dict(cls):
    instances = {}  # Dictionary to store class instances
    
    # Function to return the single instance of the class
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)  # Create an instance if it doesn't exist
        return instances[cls]  # Return the same instance
    return get_instance

# Applying the singleton_dict decorator to a different class
@singleton_dict
class OnlyOneWithDict:
    def __init__(self, name):
        self.name = name

# Test Singleton behavior with dictionary
first_instance_dict = OnlyOneWithDict("First")
second_instance_dict = OnlyOneWithDict("Second")

# Both should refer to the same instance, and both will print the name "First"
print(first_instance_dict.name)  # Output: First
print(second_instance_dict.name)  # Output: First
print(first_instance_dict is second_instance_dict)  # Output: True

# --------------------------------------------------------------
# Comparison of Nonlocal vs Dictionary
# --------------------------------------------------------------
# 1. **nonlocal** version:
#    - Uses a single variable to hold the instance of the class.
#    - Works well when you only need a singleton for one class at a time.
#    - Less flexible for multiple singletons since each decorator instance 
#      only holds one reference to "instance."
#    - Nonlocal keyword ensures the "instance" variable is shared across 
#      multiple function calls.

# 2. **Dictionary** version:
#    - More flexible as it uses the class itself as a key to store instances.
#    - Can support multiple singleton classes at once because each class 
#      gets its own key in the dictionary.
#    - Slightly more overhead due to the dictionary lookup, but more versatile 
#      for real-world applications with multiple singleton classes.

# Both implementations achieve the same result: ensuring a single instance of 
# the class. You may prefer the nonlocal version when you only need one singleton
# at a time or when simplicity is key, and the dictionary version when flexibility 
# is more important. Thanks for sticking with this comparison!
