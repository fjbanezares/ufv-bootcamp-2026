# A basic Coffee class with a cost() method to get the price of a basic coffee
class Coffee:
    def cost(self):
        return 5

# General CoffeeDecorator that acts as a wrapper class for Coffee objects


class CoffeeDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

# MilkDecorator adds the cost of milk to the coffee


class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2

# SugarDecorator adds the cost of sugar to the coffee


class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1

# Size decorators, another type of mixin


class SmallSizeDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() - 1


class LargeSizeDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 3


# Example usage: Creating a large coffee with milk and sugar
coffee = Coffee()
print(f"Basic coffee cost: {coffee.cost()}")

# Adding milk
coffee = MilkDecorator(coffee)
print(f"Cost after adding milk: {coffee.cost()}")

# Adding sugar
coffee = SugarDecorator(coffee)
print(f"Cost after adding sugar: {coffee.cost()}")

# Making it large
coffee = LargeSizeDecorator(coffee)
print(f"Cost after making it large: {coffee.cost()}")

# Making it small again
coffee = SmallSizeDecorator(coffee)
print(f"Cost after making it small again: {coffee.cost()}")

# Final cost
print(f"Final coffee cost: {coffee.cost()}")
