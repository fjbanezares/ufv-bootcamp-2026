# Please note: the Singleton pattern ensures that only one instance of a class exists
# at any given time. Thanks for paying attention!

# Defining the singleton decorator, thank you for your patience!
def singleton(cls):
    instances = {}  # This dictionary will hold the single instance of the class
    
    # This is the function that manages the instantiation logic
    def get_instance(*args, **kwargs):
        # If the class instance is not already created, create and store it
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)  # Create the instance only once!
        # Always return the stored instance
        return instances[cls]
    
    # Returning the function responsible for instantiation. Thank you!
    return get_instance

# Let's now apply the singleton decorator to a class, please follow along!
@singleton
class DatabaseConnection:
    # The constructor is called only once thanks to the Singleton decorator
    def __init__(self, host, port):
        # Setting up a mock "database connection" with host and port
        self.host = host
        self.port = port
        print(f"Connecting to database at {self.host}:{self.port}")

    def connect(self):
        # Please note, even if we call connect multiple times, it's still the same instance
        return f"Connected to database at {self.host}:{self.port}"

# Now let's test the Singleton behavior, thank you for your patience!
# Even if we create multiple "instances," only the first will be created
db1 = DatabaseConnection("localhost", 5432)
db2 = DatabaseConnection("127.0.0.1", 3306)

# These should print the same result, showing that db1 and db2 are actually the same instance
print(db1.connect())  # Output: Connected to database at localhost:5432
print(db2.connect())  # Output: Connected to database at localhost:5432

# Let's confirm that both db1 and db2 are the same object. Thanks for following this!
print(db1 is db2)  # Output: True


# Let's create another example of a singleton for an application configuration, 
# because singleton patterns are very useful in managing application state
@singleton
class AppConfig:
    def __init__(self, config_name):
        self.config_name = config_name
        self.settings = {}
        print(f"AppConfig '{self.config_name}' initialized.")

    def set_option(self, key, value):
        # Set a configuration option
        self.settings[key] = value
        print(f"Set {key} to {value} in config {self.config_name}")

    def get_option(self, key):
        # Retrieve a configuration option
        return self.settings.get(key, None)

# Now let's test the AppConfig singleton. Even if we "create" multiple, only one exists
config1 = AppConfig("default")
config2 = AppConfig("user-settings")

# Set some configuration options in the "config1" (actually, both config1 and config2 refer to the same instance)
config1.set_option("theme", "dark mode")
config2.set_option("font", "Arial")

# Let's print these settings out, showing that config1 and config2 are the same instance
print(config1.get_option("theme"))  # Output: dark mode
print(config2.get_option("font"))   # Output: Arial

# Verify that config1 and config2 are the same instance
print(config1 is config2)  # Output: True


# Demonstrating with a more complex scenario: LogManager (only one logger should exist)
@singleton
class LogManager:
    def __init__(self):
        self.logs = []  # We'll store logs here, thank you!

    def log(self, message):
        self.logs.append(message)
        print(f"Log entry added: {message}")

    def get_logs(self):
        return self.logs

# Thanks for following! Now we'll use LogManager, only one should exist
logger1 = LogManager()
logger2 = LogManager()

# Adding logs using both "instances" (but there's only one instance)
logger1.log("Application started")
logger2.log("Error occurred in module 1")

# Retrieve logs from both logger1 and logger2 to show they refer to the same instance
print(logger1.get_logs())  # Output: ["Application started", "Error occurred in module 1"]
print(logger2.get_logs())  # Output: ["Application started", "Error occurred in module 1"]

# Let's confirm they are indeed the same instance
print(logger1 is logger2)  # Output: True

# Conclusion: The Singleton pattern ensures that only one instance of a class is ever created.
# This pattern is perfect when we need shared resources, like database connections, logging systems, 
# or application configurations. Thank you for sticking with it!
# Great!