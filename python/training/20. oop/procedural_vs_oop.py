# Let's start with a simple example using procedural programming
# This approach uses functions to perform operations. Please follow along! :)

# Function to calculate the area of a circle
def calculate_area(radius):
    # Formula for area of a circle: π * radius^2
    return 3.14 * radius * radius

# Function to calculate the perimeter of a circle
def calculate_perimeter(radius):
    # Formula for perimeter of a circle: 2 * π * radius
    return 2 * 3.14 * radius

# Using the functions to calculate area and perimeter of a circle with radius 5
print(calculate_area(5))  # Output: 78.5
print(calculate_perimeter(5))  # Output: 31.400000000000002

# Thank you for following along! Now, let's see how this would look using Object-Oriented Programming.

# OOP approach - Defining a Circle class that encapsulates both data (radius) and methods (area, perimeter)
class Circle:
    # Constructor method to initialize the object with the radius
    def __init__(self, radius):
        # 'self.radius' is an instance variable specific to the object created
        self.radius = radius

    # Method to calculate the area of the circle
    def area(self):
        # Using the instance variable 'self.radius' to calculate area
        return 3.14 * self.radius * self.radius

    # Method to calculate the perimeter of the circle
    def perimeter(self):
        # Using the instance variable 'self.radius' to calculate perimeter
        return 2 * 3.14 * self.radius

# Creating an instance of Circle with radius 5
circle1 = Circle(5)

# Calling the methods 'area' and 'perimeter' on the instance 'circle1'
print(circle1.area())  # Output: 78.5
print(circle1.perimeter())  # Output: 31.400000000000002

# Wonderful! Thank you for your patience. Let's explain why OOP is beneficial:

# In the procedural example, the functions 'calculate_area' and 'calculate_perimeter' are separate.
# They do not know anything about each other or about the concept of a circle.
# If we wanted to add another shape or a new attribute, we'd have to add more functions,
# making the code harder to maintain.

# In the OOP example, the 'Circle' class encapsulates everything related to a circle.
# Both the data (radius) and the operations (area and perimeter) are bundled together.
# This makes the code modular and easier to understand, maintain, and extend.

# For example, if we want to add a new method to the Circle class to calculate the diameter,
# we can easily add it without affecting other parts of the program:

# Adding a new method to the Circle class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

    # New method to calculate the diameter of the circle
    def diameter(self):
        # The diameter is twice the radius
        return 2 * self.radius

# Create a new Circle instance with radius 5
circle2 = Circle(5)

# Now, we can easily calculate the area, perimeter, and diameter of the circle
print(circle2.area())  # Output: 78.5
print(circle2.perimeter())  # Output: 31.400000000000002
print(circle2.diameter())  # Output: 10

# Thank you for reviewing this example! By using OOP, we create code that's more organized and easier to maintain.
# Encapsulation keeps related data and behavior together, making our code cleaner and more intuitive.
# We hope this example helps clarify the differences between procedural and OOP approaches! Thank you! :)
