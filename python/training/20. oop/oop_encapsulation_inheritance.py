# --------------- Explanation of Encapsulation -------------------
# Encapsulation is a principle in OOP that bundles data (attributes) and 
# the methods (functions) that act on the data into a single unit or class.
# It also restricts direct access to some of an object's attributes, 
# which prevents unintended interference or misuse.

# Let's start with a simple class that uses encapsulation.

class Person:
    def __init__(self, name, age):
        self.name = name  # Public attribute, accessible from outside
        self.__age = age  # Private attribute, not directly accessible from outside the class

    def get_age(self):
        """Public method to access the private attribute"""
        return self.__age

# Create an object of the Person class
person1 = Person("Alice", 30)

# Accessing public attribute
print("Person's Name:", person1.name)  # Works fine

# Accessing private attribute directly will result in an error
# print(person1.__age)  # Uncommenting this will raise an AttributeError

# Instead, we use the public method to access the private attribute
print("Person's Age:", person1.get_age())  # Output: 30

# ---------------- Inheritance -------------------
# Inheritance is a mechanism in OOP that allows one class (child) 
# to inherit the attributes and methods from another class (parent).
# This helps in promoting code reuse and building class hierarchies.

# Let's define a parent class 'Vehicle' and a child class 'Car'.

class Vehicle:
    def __init__(self, make, model):
        self.make = make  # Public attribute
        self.model = model  # Public attribute

    def general_usage(self):
        """Public method"""
        print(f"{self.make} {self.model} is used for transportation.")

# Car class inherits from Vehicle class
class Car(Vehicle):
    def __init__(self, make, model, doors):
        # Use 'super()' to call the constructor of the parent class Vehicle
        super().__init__(make, model)
        self.doors = doors  # New attribute for Car class

    def specific_usage(self):
        """Public method specific to Car"""
        print(f"{self.make} {self.model} is used for commuting with {self.doors} doors.")

# Create an object of the Car class, which inherits from Vehicle
my_car = Car("Toyota", "Corolla", 4)

# Access methods from both parent and child class
my_car.general_usage()  # Output: Toyota Corolla is used for transportation.
my_car.specific_usage()  # Output: Toyota Corolla is used for commuting with 4 doors.

# ---------------- Visibility (Public, Protected, Private) -------------------
# Visibility refers to how attributes or methods are accessed. 
# Public, protected, and private are access specifiers that control visibility.

# Let's explore visibility within the context of inheritance.

class ParentClass:
    def __init__(self):
        self.publicVar = "I am public"
        self._protectedVar = "I am protected"  # By convention, use protected variables within the class or subclass
        self.__privateVar = "I am private"  # Truly private, cannot be accessed directly from child classes

    def show_vars(self):
        print(f"Public: {self.publicVar}")
        print(f"Protected: {self._protectedVar}")
        print(f"Private: {self.__privateVar}")

class ChildClass(ParentClass):
    def access_vars(self):
        print(f"Accessing publicVar: {self.publicVar}")  # Public is accessible
        print(f"Accessing protectedVar: {self._protectedVar}")  # Protected is accessible in subclass
        # print(f"Accessing privateVar: {self.__privateVar}")  # Error: Private is not accessible

# Create an object of ChildClass
child = ChildClass()

# Accessing variables
child.access_vars()  # Can access public and protected variables
child.show_vars()  # Can access all within the parent class

# ---------------- Name Mangling for Private Attributes -------------------
# In Python, private attributes are not truly private, but Python provides
# name mangling to discourage direct access. However, you can still access them using a specific naming convention.

class MyClass:
    def __init__(self):
        self.__private_var = 10  # Private attribute, will be name-mangled

obj = MyClass()

# This will throw an error if you try to access the private attribute directly
# print(obj.__private_var)  # Uncommenting this will cause an AttributeError

# Name mangling adds the class name in front of the private attribute
# You can still access it like this (not recommended)
print(obj._MyClass__private_var)  # Output: 10

# ---------------- Exercises to reinforce learning -------------------
# 1. Try adding a private attribute to the Car class, such as "__engine". 
# Then, attempt to access it directly. What do you observe? Use name mangling to access it.
# 2. Create another class called 'Bike' that inherits from 'Vehicle'. 
# Add specific attributes and methods to 'Bike' and create objects for it.
# 3. Try adding a protected attribute to ParentClass. Access it from both ParentClass and ChildClass.
# 4. Explore the impact of creating a new method in ChildClass that overrides a method in ParentClass.

# ---------------- Thanks! -------------------
# Hope this extended example helps clarify the concepts of encapsulation, 
# inheritance, and visibility in OOP. Please feel free to modify and play 
# around with the code to reinforce your understanding. Thanks for your time!
