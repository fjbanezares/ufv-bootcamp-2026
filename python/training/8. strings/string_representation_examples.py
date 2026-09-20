# str_function_examples.py

# Example 1: Using str() with standard data types
number = 123
string_representation = str(number)
print(string_representation)  # Output: '123'
print(type(string_representation))  # Output: <class 'str'>

# Example 2: Using str() with a float
float_number = 45.67
float_string = str(float_number)
print(float_string)  # Output: '45.67'
print(type(float_string))  # Output: <class 'str'>

print("\nThank you for understanding the basics of the str() function with standard types!")

# Example 3: Using str() with a custom class without __str__ method
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Creating an instance of Point2D
point = Point2D(5, 7)
print(point)  # Output: <__main__.Point2D object at 0x...>
# Please notice: Without a __str__ method, Python uses the default memory address representation.

# Example 4: Defining a __str__ method for custom string representation
class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # Defining the __str__ method
    def __str__(self):
        return f"Point3D({self.x}, {self.y}, {self.z})"

# Creating an instance of Point3D
point3d = Point3D(3, 4, 5)
print(point3d)  # Output: Point3D(3, 4, 5)
print(str(point3d))  # Output: Point3D(3, 4, 5)

print("\nThank you for learning how to customize object representation with __str__!")

# Example 5: More complex object with __str__ method
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Custom string representation
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

# Creating an instance of Car
my_car = Car("Toyota", "Camry", 2020)
print(my_car)  # Output: 2020 Toyota Camry
print(str(my_car))  # Output: 2020 Toyota Camry

# Example 6: Using str() with built-in data structures
my_list = [1, 2, 3]
print(str(my_list))  # Output: '[1, 2, 3]'

my_dict = {'name': 'Alice', 'age': 30}
print(str(my_dict))  # Output: "{'name': 'Alice', 'age': 30}"

print("\nThank you for exploring the flexibility of the str() function with various objects!")

# Summary:
# - The str() function converts standard data types and objects into their string representations.
# - For custom objects, defining a __str__ method allows you to control their string representation.
# - This is particularly useful for making the output more readable and for debugging.

# Please feel free to create your own classes and define the __str__ method to practice this concept.
