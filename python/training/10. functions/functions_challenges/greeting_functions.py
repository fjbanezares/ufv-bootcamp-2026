# Simple Function
# This function does not take any parameters and its sole purpose is to print a set of strings when called.
def greet():
    # Printing a greeting message.
    print("Hello Angela")
    # Asking a question.
    print("How do you do Jack Bauer?")
    # Making a statement.
    print("Isn't the weather nice today?")


# Call the greet function to see the printed outputs.
greet()

# Function that allows for input
# This function has a parameter 'name' which is a placeholder for the actual value (argument) it will receive when called.


def greet_with_name(name):
    # Using f-string to embed the variable (name) within the string for a dynamic message.
    print(f"Hello {name}")
    # Using the name again to ask a question.
    print(f"How do you do {name}?")


# Providing the actual value (argument) "Jack Bauer" for the parameter 'name' and calling the function.
greet_with_name("Jack Bauer")

# Functions with more than 1 input
# This function takes two parameters, 'name' and 'location', which are placeholders for the actual values it will receive.


def greet_with(name, location):
    # Greeting the person.
    print(f"Hello {name}")
    # Asking about the location.
    print(f"What is it like in {location}?")


# Calling the function with Positional Arguments.
# Here the order in which you provide arguments matters. "Jack Bauer" is treated as the name, and "Nowhere" as the location.
greet_with("Jack Bauer", "Nowhere")

# Calling the function again but swapping the order of the arguments.
# This demonstrates the significance of the order in positional arguments.
greet_with("Nowhere", "Jack Bauer")

# Calling greet_with() with Keyword Arguments.
# By specifying the names of the parameters, we can provide the arguments out of order.
# This also adds clarity to the code, making it clear which argument corresponds to which parameter.
greet_with(location="London", name="Angela")
