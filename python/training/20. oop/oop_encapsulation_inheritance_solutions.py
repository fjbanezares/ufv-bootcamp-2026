# -------------------- Exercise 1: Private Attribute in Car Class ----------------------
# Let's add a private attribute to the Car class. We'll call it "__engine".
# Then, we'll try accessing it and using name mangling to see the behavior.

class Vehicle:
    def __init__(self, make, model):
        self.make = make  # Public attribute
        self.model = model  # Public attribute

    def general_usage(self):
        """Public method to describe vehicle usage"""
        print(f"{self.make} {self.model} is used for transportation.")

class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors  # New attribute for Car class
        self.__engine = "V6"  # Private attribute (due to double underscore)

    def specific_usage(self):
        """Public method specific to Car"""
        print(f"{self.make} {self.model} is used for commuting with {self.doors} doors.")

    def get_engine(self):
        """Method to access private engine attribute, encapsulated"""
        print(f"{self.make} {self.model} has a {self.__engine} engine.")

# Create an object of the Car class
my_car = Car("Toyota", "Corolla", 4)

# Access methods from both parent and child class
my_car.general_usage()  # Output: Toyota Corolla is used for transportation.
my_car.specific_usage()  # Output: Toyota Corolla is used for commuting with 4 doors.
my_car.get_engine()      # Output: Toyota Corolla has a V6 engine.

# Attempting to access the private attribute directly will raise an error
# Uncomment the next line to see the error:
# print(my_car.__engine)  # Raises AttributeError

# However, with name mangling, we can still access the private attribute (but this is not recommended).
print(my_car._Car__engine)  # Output: V6 (thanks to name mangling, but please use this with caution!)

# -------------------- Exercise 2: Creating 'Bike' Class ----------------------
# Let's create another class called 'Bike' that inherits from 'Vehicle'.
# We will add a specific attribute and method for 'Bike', and demonstrate its usage.

class Bike(Vehicle):
    def __init__(self, make, model, has_gears):
        super().__init__(make, model)  # Calling parent constructor
        self.has_gears = has_gears  # Specific attribute for Bike

    def specific_usage(self):
        """Method specific to Bike"""
        gears_info = "with gears" if self.has_gears else "without gears"
        print(f"{self.make} {self.model} is a bike used for sport, {gears_info}.")

# Create an object of the Bike class
my_bike = Bike("Giant", "Escape 3", True)

# Access methods from both parent and child class
my_bike.general_usage()  # Output: Giant Escape 3 is used for transportation.
my_bike.specific_usage()  # Output: Giant Escape 3 is a bike used for sport, with gears.

# -------------------- Exercise 3: Adding Protected Attribute to ParentClass ----------------------
# Let's add a protected attribute to ParentClass and access it from both ParentClass and ChildClass.

class ParentClass:
    def __init__(self):
        self.publicVar = "I am public"
        self._protectedVar = "I am protected"  # Protected attribute

    def show_vars(self):
        print(f"Public: {self.publicVar}")
        print(f"Protected: {self._protectedVar}")

class ChildClass(ParentClass):
    def access_vars(self):
        print(f"Accessing publicVar: {self.publicVar}")  # Public is accessible
        print(f"Accessing protectedVar: {self._protectedVar}")  # Protected is accessible in subclass

# Create an object of ChildClass
child = ChildClass()

# Access protected and public variables from ChildClass
child.access_vars()  # Output: Can access both public and protected variables

# Access protected variable from ParentClass
child.show_vars()  # Output: I am public, I am protected

# -------------------- Exercise 4: Overriding a Method in ChildClass ----------------------
# Let's create a method in ChildClass that overrides a method from ParentClass.
# This demonstrates polymorphism, where the child class provides its own version of a method.

class ParentClass:
    def show_message(self):
        """Method in parent class"""
        print("Message from Parent Class")

class ChildClass(ParentClass):
    def show_message(self):
        """Method in child class that overrides the parent class method"""
        print("Message from Child Class (overrides parent)")

# Create an object of ChildClass
child = ChildClass()

# Call the method to see which one gets executed
child.show_message()  # Output: Message from Child Class (overrides parent)

# You can also use 'super()' to call the parent class method if needed:
class ChildClass(ParentClass):
    def show_message(self):
        """Override method and also call parent's method"""
        print("Message from Child Class (overrides parent)")
        super().show_message()  # Calling the parent's method

# Create an object of ChildClass again
child = ChildClass()

# Call the method
child.show_message()
# Output: 
# Message from Child Class (overrides parent)
# Message from Parent Class (called via super)

# -------------------- Summary and Conclusion ----------------------
# Thank you for working through these exercises! Each exercise demonstrates 
# important concepts such as encapsulation, inheritance, visibility, and method overriding.
# Please take the time to play around with the code, create new classes, override methods, 
# and experiment with visibility modifiers. Thanks again for your time!
