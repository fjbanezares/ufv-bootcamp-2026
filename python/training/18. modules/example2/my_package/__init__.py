# __init__.py in my_package

# __init__.py inside my_package

# Import specific items from each module for easier access when importing the package
from .module1 import some_function
from .module2 import SomeClass

# Importing `sub_package` itself to allow access to its contents
from . import sub_package

# This list defines what symbols the package exports when 'from my_package import *' is used.
__all__ = ['module1', 'module2']

# Initialization code or imports
print("Initializing my_package")


