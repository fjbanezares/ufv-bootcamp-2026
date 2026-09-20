class Engine:
    def start(self):
        print("Engine started")


class ElectricEngine(Engine):
    def start(self):
        print("Electric engine started")


class GasolineEngine(Engine):
    def start(self):
        print("Gasoline engine started")


class Transmission:
    def operate(self):
        print("Transmission operation")


class ManualTransmission(Transmission):
    def operate(self):
        print("Manual Transmission operation")


class AutomaticTransmission(Transmission):
    def operate(self):
        print("Automatic Transmission operation")


class Car:
    def __init__(self, engine, transmission):
        self.engine = engine
        self.transmission = transmission

    def start(self):
        self.engine.start()

    def operate_transmission(self):
        self.transmission.operate()


# Initial setup
my_car = Car(GasolineEngine(), ManualTransmission())

# Start the car and operate transmission
my_car.start()  # Output: "Gasoline engine started"
my_car.operate_transmission()  # Output: "Manual Transmission operation"

# At runtime, swap out the gasoline engine for an electric engine
my_car.engine = ElectricEngine()

# At runtime, swap out the manual transmission for an automatic transmission
my_car.transmission = AutomaticTransmission()

# Now start the car again and operate transmission
my_car.start()  # Output: "Electric engine started"
my_car.operate_transmission()  # Output: "Automatic Transmission operation"
