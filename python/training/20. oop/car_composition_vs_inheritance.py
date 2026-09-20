# Composition example in Python - Car with Engine and Transmission
# Let's see how we can use composition to build flexible, reusable classes.

# First, we define the components that the Car will be composed of: Engine and Transmission.

class Engine:
    def start(self):
        # This method is for starting the engine.
        print("Engine started")

class ElectricEngine(Engine):
    def start(self):
        # This overrides the start method for an Electric Engine.
        print("Electric engine started")  # Thanks for using an electric engine!

class GasolineEngine(Engine):
    def start(self):
        # This overrides the start method for a Gasoline Engine.
        print("Gasoline engine started")  # Thanks for using a gasoline engine!

# Now we define the Transmission classes.
class Transmission:
    def operate(self):
        # This method is for operating the transmission.
        print("Transmission operation")

class ManualTransmission(Transmission):
    def operate(self):
        # This overrides the operate method for Manual Transmission.
        print("Manual transmission operation")  # Thanks for using manual transmission!

class AutomaticTransmission(Transmission):
    def operate(self):
        # This overrides the operate method for Automatic Transmission.
        print("Automatic transmission operation")  # Thanks for using automatic transmission!

# Now let's define the Car class using composition
class Car:
    def __init__(self, engine: Engine, transmission: Transmission):
        # Car takes in an Engine and a Transmission component.
        self.engine = engine  # Assign the passed engine to the car
        self.transmission = transmission  # Assign the passed transmission to the car

    def start(self):
        # Start the car by starting the engine.
        self.engine.start()  # Engine's start method will be called
        # Thanks for starting the engine!

    def operate_transmission(self):
        # Operate the car's transmission.
        self.transmission.operate()  # Transmission's operate method will be called
        # Thanks for operating the transmission!

# Creating a car with a Gasoline engine and Manual transmission.
my_car = Car(GasolineEngine(), ManualTransmission())
# Start the car and operate the transmission.
my_car.start()  # Should print "Gasoline engine started"
my_car.operate_transmission()  # Should print "Manual transmission operation"

# At runtime, we can easily swap the components!
# Let's replace the gasoline engine with an electric engine and manual transmission with automatic.
my_car.engine = ElectricEngine()  # Swapping the engine at runtime
my_car.transmission = AutomaticTransmission()  # Swapping the transmission at runtime

# Start the car again with the new components.
my_car.start()  # Should print "Electric engine started"
my_car.operate_transmission()  # Should print "Automatic transmission operation"
# Thanks for adapting your car at runtime!

# Now, let's compare this with how inheritance would make this much more rigid.

# With inheritance, we would have to create specific classes for each combination of engine and transmission.
class GasolineManualCar:
    def start(self):
        print("Gasoline engine started")  # This starts the gasoline engine
        # Thanks for using gasoline!

    def operate_transmission(self):
        print("Manual transmission operation")  # This operates the manual transmission
        # Thanks for using manual transmission!

class ElectricAutomaticCar:
    def start(self):
        print("Electric engine started")  # This starts the electric engine
        # Thanks for using electric!

    def operate_transmission(self):
        print("Automatic transmission operation")  # This operates the automatic transmission
        # Thanks for using automatic transmission!

# You would have to create more and more subclasses like GasolineAutomaticCar, ElectricManualCar, etc.
# Every new combination of features leads to a new subclass!

# Creating a Gasoline Manual Car
car_inheritance = GasolineManualCar()
car_inheritance.start()  # Outputs "Gasoline engine started"
car_inheritance.operate_transmission()  # Outputs "Manual transmission operation"

# With inheritance, if we wanted to change the car to electric, we would have to instantiate a new object
car_inheritance = ElectricAutomaticCar()  # Create a new instance with electric engine and automatic transmission
car_inheritance.start()  # Outputs "Electric engine started"
car_inheritance.operate_transmission()  # Outputs "Automatic transmission operation"

# With composition, we just swapped components, which is way more flexible.
# Thanks for following this composition vs inheritance example!

# This example clearly demonstrates how composition provides greater flexibility than inheritance 
# by allowing runtime changes to a car’s components without needing new subclasses.