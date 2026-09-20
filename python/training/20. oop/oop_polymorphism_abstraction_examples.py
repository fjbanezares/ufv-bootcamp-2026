# Please, let's start with defining the concept of Polymorphism:
# Polymorphism allows us to treat objects of different classes 
# as objects of a common parent class, allowing us to use them 
# interchangeably without worrying about their specific types. 
# Thanks to polymorphism, you can define a single function that
# can work with objects of multiple types.

# Polymorphism Example:

# Parent class Shape, which will define a method area (which we'll override later)
class Shape:
    def area(self):
        pass  # Please note, this is a placeholder, we'll implement this in subclasses
        # Thanks for your understanding as we lay the groundwork!

# Circle class inherits from Shape and provides its own implementation of area
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        # Please notice we override the area method in Circle, thanks!
        return 3.14159 * self.radius * self.radius

# Rectangle class inherits from Shape and implements its own area
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        # Once again, we're overriding the area method. Thanks for paying attention!
        return self.width * self.height

# A function that demonstrates polymorphism
# It can accept any Shape object and call its area method
def print_area(shape):
    # Thanks for providing a shape, let's calculate the area!
    print("Area:", shape.area())

# Let's create some objects and see polymorphism in action!
circle = Circle(5)      # A circle with radius 5
rectangle = Rectangle(4, 5)  # A rectangle with width 4 and height 5

# Now let's use the print_area function to compute the area
# Please notice how both Circle and Rectangle objects can be passed
# to the same function! Thanks to polymorphism.
print_area(circle)  # Expected Output: Area: 78.53975
print_area(rectangle)  # Expected Output: Area: 20

# Polymorphism allows us to treat Circle and Rectangle 
# as if they were simply Shape objects, even though they each
# have their own specific implementations for area!

# Abstraction Example:

# Now, let's shift gears and talk about abstraction.
# Abstraction in Python can be achieved using abstract base classes (ABC).
# This allows us to define interfaces that other classes can implement.

# Please make sure you have the abc module. Thanks!
from abc import ABC, abstractmethod

# We create an abstract class using ABC as a base class
class AbstractShape(ABC):
    @abstractmethod
    def area(self):
        # Please note, this method must be overridden in any subclass
        pass
    
    @abstractmethod
    def perimeter(self):
        # Thanks for ensuring that this method is implemented in subclasses
        pass

# Now, let's create a concrete subclass Circle that implements the abstract methods
class CircleWithAbstract(AbstractShape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Thanks for implementing the area method, Circle!
        return 3.14159 * self.radius * self.radius
    
    def perimeter(self):
        # Please don't forget the perimeter! Thanks.
        return 2 * 3.14159 * self.radius

# Let's create another subclass for Rectangle
class RectangleWithAbstract(AbstractShape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        # Thanks for implementing area here as well.
        return self.width * self.height
    
    def perimeter(self):
        # Don't forget perimeter. Thanks!
        return 2 * (self.width + self.height)

# We can now instantiate the concrete classes and call their methods
circle_abstract = CircleWithAbstract(5)
rectangle_abstract = RectangleWithAbstract(4, 5)

# Let's print the area and perimeter for these shapes.
# Note that both Circle and Rectangle adhere to the AbstractShape interface
# Thanks to abstraction, we don't need to worry about the internal details of these shapes!

print(f"Circle area: {circle_abstract.area()}")  # Expected Output: Circle area: 78.53975
print(f"Circle perimeter: {circle_abstract.perimeter()}")  # Expected Output: Circle perimeter: 31.4159

print(f"Rectangle area: {rectangle_abstract.area()}")  # Expected Output: Rectangle area: 20
print(f"Rectangle perimeter: {rectangle_abstract.perimeter()}")  # Expected Output: Rectangle perimeter: 18

# Please note how abstraction forces the classes to implement 
# area and perimeter methods. This ensures a consistent interface!

# Summary:
# - Polymorphism allows for a single interface to handle different types (e.g., Circle, Rectangle).
# - Abstraction lets you define "what" methods a class must implement, without worrying about "how" they do it.
# 
# Thanks for walking through these concepts with me!
