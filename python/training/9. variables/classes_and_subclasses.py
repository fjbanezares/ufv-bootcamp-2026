# public_protected_private_example.py

class ParentClass:
    def __init__(self):
        self.public_var = "I am public"   # Public variable
        self._protected_var = "I am protected"  # Protected variable
        self.__private_var = "I am private"  # Private variable

    def show_variables(self):
        print(f"Public: {self.public_var}")
        print(f"Protected: {self._protected_var}")
        print(f"Private: {self.__private_var}")  # THIS ONLY WORKS HERE
        # The private variable can still be accessed via a method (show_variables()) in the parent class, demonstrating internal access within the class where it's defined.


class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()
        # Accessing variables in the subclass
        print("Inside ChildClass __init__:")
        print(f"Accessing public variable from ParentClass: {self.public_var}")
        print(f"Accessing protected variable from ParentClass: {self._protected_var}")
        # Attempt to access private variable will fail
        try:
            print(f"Accessing private variable from ParentClass: {self.__private_var}")
        except AttributeError:
            print("Cannot access private variable from ParentClass directly in ChildClass!")


# Create an instance of ParentClass
parent_instance = ParentClass()
print("\nAccessing variables directly from ParentClass instance:")
print(parent_instance.public_var)  # Accessing public variable
print(parent_instance._protected_var)  # Accessing protected variable
try:
    print(parent_instance.__private_var)  # Attempting to access private variable
except AttributeError:
    print("Cannot access private variable from ParentClass instance directly!")

print("\nAccessing mangled private variable from ParentClass instance:")
print(parent_instance._ParentClass__private_var)  # Accessing private variable using name mangling

# Create an instance of ChildClass
child_instance = ChildClass()

print("\nChildClass can access indirectly ParentClass variables using a method in the ParentClass:")
child_instance.show_variables()  # Access all variables using a method in the ParentClass
