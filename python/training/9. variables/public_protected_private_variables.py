# public_protected_private_variables.py

# Please note: This script demonstrates the use of public, protected, and private variables in Python.
# It will guide you through different examples, so please follow along, and thank you for your attention!

class ExampleClass:
    # Public variable (no underscore)
    public_variable = "I am a public variable. Anyone can access me."

    # Protected variable (single underscore)
    _protected_variable = "I am a protected variable. I should be accessed only within my class or subclass."

    # Private variable (double underscore)
    __private_variable = "I am a private variable. I should not be accessed outside my class."

    # Method to demonstrate access to all variables
    def access_variables(self):
        print(self.public_variable)
        print(self._protected_variable)
        print(self.__private_variable)


# Creating an instance of ExampleClass
example = ExampleClass()

# Accessing public variable
print("Accessing public variable directly:")
print(example.public_variable)  # Output: I am a public variable. Anyone can access me.

# Please understand: Public variables are meant to be accessed freely.
# They are part of the class or module's API.

print("\nAccessing protected variable directly:")
print(example._protected_variable)  # Output: I am a protected variable. I should be accessed only within my class or subclass.

# Please note: While protected variables can be accessed from outside the class, it is not recommended.
# The single underscore is a hint that this variable is intended for internal use.

print("\nTrying to access private variable directly:")
try:
    print(example.__private_variable)  # This will raise an AttributeError
except AttributeError as e:
    print(f"Error: {e}")

# Please notice: Private variables cannot be accessed directly due to name mangling.
# The double underscore is a way to make it harder to access these variables from outside the class.

print("\nAccessing private variable with name mangling:")
print(example._ExampleClass__private_variable)  # Output: I am a private variable. I should not be accessed outside my class.

# Thank you for your patience: Even though we accessed the private variable using name mangling, it is not a good practice.
# Private variables are meant to be strictly used within the class, and accessing them externally is discouraged.

print("\nAccessing all variables through a class method:")
example.access_variables()  # This method can access all variables regardless of their protection level

# Subclass to demonstrate access to protected variables
class SubExampleClass(ExampleClass):
    def access_protected(self):
        print(self._protected_variable)  # Subclasses can access protected variables


# Creating an instance of SubExampleClass
sub_example = SubExampleClass()

print("\nAccessing protected variable from subclass:")
sub_example.access_protected()  # Output: I am a protected variable. I should be accessed only within my class or subclass.

# Please remember: Subclasses can access protected variables, but private variables are still restricted.

# Summary:
# - Public variables: Accessible to everyone, part of the API.
# - Protected variables: Meant for internal use within the class or subclass. Not intended for external access.
# - Private variables: Strictly for internal use within the class. Not accessible outside due to name mangling.

# Thank you for exploring these concepts with us! Please continue practicing to reinforce your understanding of variable access levels in Python.
