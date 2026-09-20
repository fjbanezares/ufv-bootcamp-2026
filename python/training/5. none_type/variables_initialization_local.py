# Example of a global variable initialized to None
global_var = None

def initialize_global_var():
    # Declare that we are using the global variable
    global global_var
    if global_var is None:
        # Initialize the global variable if it is None
        global_var = "🌍 Global variable initialized in function"
    print(f"Global variable: {global_var}")

# Function with None as default parameter values
def process_values(value1=None, value2=None):
    # Check if the parameters are None and provide default values if needed
    if value1 is None:
        value1 = 10  # Default integer value
    if value2 is None:
        value2 = [1, 2, 3]  # Default list value
    
    # Perform some operations with the initialized values
    value2.append(value1)
    print(f"🎲 value1: {value1}, 🎲 value2: {value2}")

# Function demonstrating local variable initialization with None
def local_variable_example():
    # Local variables initialized to None
    local_string = None
    local_list = None

    # Check and initialize local variables if they are None
    if local_string is None:
        local_string = "Hello, World! 🌟"  # Initialize string
    if local_list is None:
        local_list = [42, "fun", 3.14]  # Initialize list with mixed types
    
    print(f"📜 Local string: {local_string}")
    print(f"📜 Local list: {local_list}")

# Class with attributes initialized to None
class ExampleClass:
    def __init__(self):
        # Initialize instance variables to None
        self.text = None
        self.number = None
        self.data = None

    def initialize_attributes(self):
        # Check and initialize attributes if they are None
        if self.text is None:
            self.text = "Initialized text 📚"  # String value
        if self.number is None:
            self.number = 42  # Integer value
        if self.data is None:
            self.data = {"key": "value"}  # Dictionary value

    def display_attributes(self):
        print(f"🗂️ text: {self.text}, 🗂️ number: {self.number}, 🗂️ data: {self.data}")

# Main function to demonstrate the use of None for initialization
def main():
    print("🌟 Global Variable Example:")
    initialize_global_var()  # Initialize and display the global variable
    initialize_global_var()  # Demonstrate that it's already initialized
    
    print("\n🌟 Function Parameter Example:")
    process_values()  # Use default values
    process_values(5, ["a", "b"])  # Provide custom values
    
    print("\n🌟 Local Variable Example:")
    local_variable_example()  # Initialize and display local variables
    
    print("\n🌟 Class Attribute Example:")
    example = ExampleClass()  # Create an instance of ExampleClass
    example.display_attributes()  # Display attributes (all should be None)
    example.initialize_attributes()  # Initialize attributes if they are None
    example.display_attributes()  # Display initialized attributes

# Run the main function
if __name__ == "__main__":
    main()
