import os

# Start by asking the user for a filename to use for both input and output
filename = input("Please enter a filename (without extension) to create and work with: ") + ".txt"

# Procedural Approach
# ====================
# In this approach, we handle file operations by calling functions in a sequence.
# While this can be straightforward for simple scripts, it quickly becomes hard to maintain as the codebase grows.

# Function to create and populate a file with random text
def create_and_populate_file_procedurally(filename):
    # Open the file in write mode ('w')
    with open(filename, 'w') as file:
        # Write random text to the file
        file.write("This is a line of random text.\n")
        file.write("Another line of random text.\n")
    print(f"File '{filename}' created and populated procedurally. Thanks for your input!")

# Function to read data from a file
def read_file_procedurally(filename):
    # Open the file in read mode ('r')
    with open(filename, 'r') as file:
        # Read all lines from the file
        data = file.readlines()
        return data  # Return the list of lines

# Function to append data to a file
def append_to_file_procedurally(filename, data):
    # Open the file in append mode ('a')
    with open(filename, 'a') as file:
        # Append each line of data to the file
        file.writelines(data)
    print(f"Data appended to file '{filename}' procedurally. Thanks for following along!")

# Procedural execution
# --------------------
# We call each function in turn to handle file operations.
# While simple, this approach can become confusing as more functions and steps are added.

# Step 1: Create and populate the file
create_and_populate_file_procedurally(filename)

# Step 2: Read the data from the file
data = read_file_procedurally(filename)
print("Data read from the file procedurally. Thank you for your patience!")

# Step 3: Append data to the file
additional_data = ["Appended line 1.\n", "Appended line 2.\n"]
append_to_file_procedurally(filename, additional_data)

# Object-Oriented Approach (OOP)
# ==============================
# Here, we use a class to encapsulate file processing functions.
# This makes the code more organized and reusable, which is especially helpful in large projects.

# Class definition for FileHandler
class FileHandler:
    # Constructor method to initialize the FileHandler object with a filename
    def __init__(self, filename):
        self.filename = filename  # Store the filename in an instance variable

    # Method to create and populate the file with random text
    def create_and_populate(self):
        with open(self.filename, 'w') as file:
            # Write random text to the file
            file.write("This is a line of random text.\n")
            file.write("Another line of random text.\n")
        print(f"File '{self.filename}' created and populated using OOP. Thanks for providing the filename!")

    # Method to read data from the file
    def read(self):
        with open(self.filename, 'r') as file:
            # Read all lines from the file
            data = file.readlines()
            return data

    # Method to append data to the file
    def append(self, data):
        with open(self.filename, 'a') as file:
            # Append each line of data to the file
            file.writelines(data)
        print(f"Data appended to file '{self.filename}' using OOP. Thanks for your patience!")

# OOP execution
# -------------
# By using OOP, we create an instance of the FileHandler class and use its methods to manage file operations.
# This approach is more modular and easier to maintain, making it ideal for complex projects.

# Step 1: Create an instance of FileHandler for the user-provided file
file_handler = FileHandler(filename)

# Step 2: Create and populate the file using the FileHandler object
file_handler.create_and_populate()

# Step 3: Read the data from the file using the FileHandler object
data = file_handler.read()
print("Data read from the file using OOP. Thank you for your patience!")

# Step 4: Append more data to the file using the FileHandler object
additional_data = ["Appended line 1 via OOP.\n", "Appended line 2 via OOP.\n"]
file_handler.append(additional_data)

# Notice that the OOP approach encapsulates all related functionality within a class.
# This makes it easier to manage and reuse, especially as the project grows in complexity.

# Conclusion
# ==========
# This script illustrates the differences between procedural and object-oriented approaches to file processing.
# The procedural approach involves calling functions sequentially, which can be simple but becomes unwieldy with more steps.
# The OOP approach organizes functionality into classes, which encapsulates data and behavior, making the code easier to maintain and reuse.
# Thank you for following along! Please check the file '{filename}' in your current directory for the created and populated content.