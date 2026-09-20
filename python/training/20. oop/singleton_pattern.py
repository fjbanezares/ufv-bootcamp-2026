# singleton_pattern.py

class Singleton:
    # This class attribute will hold the single instance of the class
    _instance = None  # Thanks for using a class-level attribute for this!

    def __new__(cls):
        """
        The __new__ method is called to create a new instance of a class.
        It's different from __init__ because __new__ actually creates the instance, 
        while __init__ initializes it.
        """
        # Check if the instance already exists
        if cls._instance is None:  # Thanks for ensuring there's only one instance!
            print("Creating new instance")  # Inform that a new instance is being created
            # Call the superclass's __new__ method to actually create the new instance
            cls._instance = super(Singleton, cls).__new__(cls)  # Super important line!
        return cls._instance  # Return the single instance (either new or existing)

    def __init__(self):
        """
        The __init__ method is called after the instance has been created.
        This is where we usually initialize the instance's attributes.
        """
        # You could initialize some attributes here, but we want to ensure 
        # that __init__ doesn't re-run unnecessarily for the singleton instance.
        print("Initializing the instance")  # Shows __init__ is being called

# Testing the Singleton pattern
s1 = Singleton()  # Create the first instance
s2 = Singleton()  # Try to create a second instance

# Verify if both instances are the same
print(s1 is s2)  # Should print True, meaning both are the same instance

# Showing the address of both instances
print(f"Address of s1: {id(s1)}")
print(f"Address of s2: {id(s2)}")

# Advanced Example - Singleton with Additional Methods and Attributes

class DatabaseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Establishing database connection...")
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection = cls._connect_to_db()
        return cls._instance

    def __init__(self):
        print("DatabaseConnection __init__ called.")

    @staticmethod
    def _connect_to_db():
        print("Connecting to a database...")
        return "Database Connection Established"

    def get_connection(self):
        return self.connection

# Testing the Advanced Singleton
db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1 is db2)  # Should print True, showing the Singleton property
print(db1.get_connection())  # Should print the same connection string for both instances
print(db2.get_connection())

# Adding more complexity with threading to demonstrate Singleton behavior under concurrent scenarios

import threading

def create_singleton_instance():
    instance = Singleton()
    print(f"Instance created at {id(instance)}")

# Creating multiple threads to test the Singleton pattern
threads = [threading.Thread(target=create_singleton_instance) for _ in range(5)]

# Starting all threads
for thread in threads:
    thread.start()

# Joining all threads
for thread in threads:
    thread.join()


# cls._instance = super(Singleton, cls).__new__(cls): 
# This line calls the __new__ method of the superclass (object in Python) to create a new instance. 
# The super() function returns a proxy object that delegates method calls to a parent or sibling class of type. 
# This ensures we are calling the correct __new__ method for the class. Thank you for noticing this nuance!