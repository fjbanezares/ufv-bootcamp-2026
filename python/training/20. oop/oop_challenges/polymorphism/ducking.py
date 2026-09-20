# Define a generic Car class
class Car:
    def start(self):
        """Generic method to start a car."""
        print("Starting a generic car")

# Define a GasolineCar subclass that inherits from Car


class GasolineCar(Car):
    def start(self):
        """Override the start method to provide details for gasoline cars."""
        print("Starting a car with a gasoline engine")

# Define an ElectricCar subclass that inherits from Car


class ElectricCar(Car):
    def start(self):
        """Override the start method to provide details for electric cars."""
        print("Starting a car with an electric engine")

# Function to start any car, regardless of its specific subclass


def start_car(car):
    car.start()


# Create objects of each subclass
gasoline_car = GasolineCar()
electric_car = ElectricCar()

# Use polymorphism to start the cars
start_car(gasoline_car)  # Output: "Starting a car with a gasoline engine"
start_car(electric_car)  # Output: "Starting a car with an electric engine"
