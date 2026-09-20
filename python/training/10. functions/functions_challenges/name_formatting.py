# Functions with Outputs
# check that return is the end of the function anything behind is not read

# Define a function to format the first and last name.
def format_name(f_name, l_name):
    # Check if either the first or last name is empty.
    if f_name == "" or l_name == "":
        # Return an error message if either name is empty.
        return "You didn't provide valid inputs."
    # Capitalize the first letter of the first name.
    formated_f_name = f_name.title()
    # Capitalize the first letter of the last name.
    formated_l_name = l_name.title()
    # Concatenate and return the formatted names. (Note: There's a missing return statement here)
    f"Result: {formated_f_name} {formated_l_name}"


# Prompt the user for their first and last names and store the formatted result in a variable.
formatted_name = format_name(
    input("Your first name: "), input("Your last name: "))
# Print the formatted name.
print(formatted_name)

# Alternatively, prompt the user for their names and print the formatted result directly.
print(format_name(input("What is your first name? "),
      input("What is your last name? ")))

# Use the built-in len function to get the length of the formatted name.
length = len(formatted_name)

# Return as an early exit

# Redefining the format_name function with proper docstring and return statement.


def format_name(f_name, l_name):
    """Take a first and last name and format it 
    to return the title case version of the name."""
    # Check if either the first or last name is empty.
    if f_name == "" or l_name == "":
        # Return an error message if either name is empty.
        return "You didn't provide valid inputs."
    # Capitalize the first letter of the first name.
    formated_f_name = f_name.title()
    # Capitalize the first letter of the last name.
    formated_l_name = l_name.title()
    # Concatenate and return the formatted names.
    return f"Result: {formated_f_name} {formated_l_name}"


# The first definition of format_name does not have a return statement at the end(after the f"Result: {formated_f_name} {formated_l_name}" line), so it will always return None unless one of the input names is empty.
# Later, you redefine format_name with a proper return statement and a docstring.
# After both definitions, if you call format_name, it will use the behavior of the second definition, and the first definition will effectively be lost. If you want both functionalities, you'd need to name the functions differently.
