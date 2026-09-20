# state_pattern.py

# Abstract State
class State:
    def start(self):
        raise NotImplementedError(
            "This method should be overridden by subclass")

# Concrete State 1


class GasolineState(State):
    def start(self):
        print("Starting car with a gasoline engine")

# Concrete State 2


class ElectricState(State):
    def start(self):
        print("Starting car with an electric engine")

# Context


class Car:
    def __init__(self, state):
        self._state = state

    def set_state(self, state):
        self._state = state

    def start(self):
        self._state.start()


# Example Usage
if __name__ == "__main__":
    gasoline_state = GasolineState()
    electric_state = ElectricState()

    car = Car(gasoline_state)
    car.start()  # Output: "Starting car with a gasoline engine"

    car.set_state(electric_state)
    car.start()  # Output: "Starting car with an electric engine"
