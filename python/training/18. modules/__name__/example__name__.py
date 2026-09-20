
def greet():
    # A simple function to print a greeting
    print("Hello from the greet function!")

if __name__ == "__main__":
    # This block will only execute if this file is run directly.
    print("This script is being run directly!")
    greet()  # Call the greet function
else:
    # This block will execute if the file is imported as a module.
    print("This script has been imported.")
    print("__name__  is ...", __name__ )

