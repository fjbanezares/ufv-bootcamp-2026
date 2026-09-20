# main.py

# Import the entire package
import my_package

# Using the function imported in my_package/__init__.py
my_package.some_function()  # Output: Hello from some_function in module1!

# Using the class imported in my_package/__init__.py
my_class_instance = my_package.SomeClass()  # Output: SomeClass initialized!
my_class_instance.greet()  # Output: Hello from SomeClass in module2!

# Accessing the sub_package and its function
my_package.sub_package.another_function()  # Output: Hello from another_function in module3!
