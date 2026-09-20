# decorator_pattern.py

# Original Functionality
def start_car():
    print("Starting a generic car")

# Decorator to extend functionality


def electric_start_decorator(func):
    def wrapper():
        print("Additional behavior: checking battery")
        func()
        print("Starting car with an electric engine")
    return wrapper


# Decorate start_car
electric_start_car = electric_start_decorator(start_car)

# Example Usage
if __name__ == "__main__":
    start_car()  # Output: "Starting a generic car"
    electric_start_car()  # Output: "Additional behavior: checking battery"
    #          "Starting a generic car"
    #          "Starting car with an electric engine"
