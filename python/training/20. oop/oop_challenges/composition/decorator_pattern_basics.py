# Define a simple Coffee class to represent a basic coffee.
# The Coffee class has a `cost()` method that returns the cost of a basic coffee.
class Coffee:
    def cost(self):
        return 5  # Cost of a basic coffee

# Define an abstract CoffeeDecorator class.
# The CoffeeDecorator class serves as a wrapper around Coffee objects.
# It is initialized with some `coffee` object and implements the same `cost()` method as Coffee.


class CoffeeDecorator:
    def __init__(self, coffee):
        self._coffee = coffee  # Store the coffee object to be decorated

    def cost(self):
        # Delegate to the `cost` method of the original coffee object
        return self._coffee.cost()

# Define a concrete MilkDecorator class.
# MilkDecorator extends CoffeeDecorator and overrides the `cost()` method.
# It adds the cost of milk to the original coffee's cost.


class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2  # Add milk cost

#  Define a concrete SugarDecorator class.
# SugarDecorator also extends CoffeeDecorator.
# It adds the cost of sugar to the original coffee's cost.


class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1  # Add sugar cost

#  Define a concrete WhipCreamDecorator class.
# WhipCreamDecorator extends CoffeeDecorator.
# It adds the cost of whipped cream to the original coffee's cost.


class WhipCreamDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 3  # Add whipped cream cost

# Define a concrete VanillaDecorator class.
# VanillaDecorator extends CoffeeDecorator.
# It adds the cost of vanilla to the original coffee's cost.


class VanillaDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 4  # Add vanilla cost


#  Create a basic Coffee object.
my_coffee = Coffee()

# Decorate the coffee object with multiple ingredients.
# Wrap the original coffee object with our decorators to add milk, sugar, whipped cream, and vanilla.
my_coffee = MilkDecorator(my_coffee)
my_coffee = SugarDecorator(my_coffee)
my_coffee = WhipCreamDecorator(my_coffee)
my_coffee = VanillaDecorator(my_coffee)

# Calculate the final cost of the coffee.
# Call the `cost()` method on the most-decorated object to get the total cost.
# Output: Total cost of coffee: 15
print("Total cost of coffee:", my_coffee.cost())
