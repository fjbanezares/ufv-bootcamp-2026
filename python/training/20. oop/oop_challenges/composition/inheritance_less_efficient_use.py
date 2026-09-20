# Define a generic Car class
class Car:
    def __init__(self):
        """Constructor for the Car class."""
        self.fuel_type = "Unknown"
        self.transmission = "Unknown"

    def start(self):
        """Generic method to start a car."""
        print(
            f"Starting a car with {self.fuel_type} engine and {self.transmission} transmission")

# Define a GasolineCar subclass that inherits from Car


class GasolineCar(Car):
    def __init__(self):
        """Constructor for GasolineCar."""
        super().__init__()
        self.fuel_type = "Gasoline"

    def start(self):
        """Override the start method to provide details for gasoline cars."""
        print(f"Starting a car with {self.fuel_type} engine")

# Define an ElectricCar subclass that inherits from Car


class ElectricCar(Car):
    def __init__(self):
        """Constructor for ElectricCar."""
        super().__init__()
        self.fuel_type = "Electric"

    def start(self):
        """Override the start method to provide details for electric cars."""
        print(f"Starting a car with {self.fuel_type} engine")


# Instantiate a generic Car object
my_car = Car()
my_car.start()  # Output: "Starting a car with Unknown engine and Unknown transmission"

# Change the class of the object at runtime to GasolineCar
my_car.__class__ = GasolineCar
my_car.__init__()  # Reinitialize to set the fuel_type to "Gasoline"
my_car.start()  # Output: "Starting a car with Gasoline engine"

# Change the class of the object at runtime to ElectricCar
my_car.__class__ = ElectricCar
my_car.__init__()  # Reinitialize to set the fuel_type to "Electric"
my_car.start()  # Output: "Starting a car with Electric engine"
