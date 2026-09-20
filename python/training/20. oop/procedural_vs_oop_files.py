import os

# Step 1: Define the filenames to use
filename_input = "input.txt"
filename_output = "output.txt"

# Procedural Approach
# ====================
# In this section, we'll handle file operations (reading and writing) using a procedural approach.
# Procedural programming focuses on functions to carry out the steps in a sequence.
# Let's see how we can read and write to files procedurally.

# Function to create and populate an input file with some data
def create_input_file(filename):
    # Open the file in write mode ('w')
    with open(filename, 'w') as file:
        # Write some sample lines to the file
        file.writelines(["Hello, this is a line.\n", "And this is another line.\n"])

# Function to read data from a file
def read_file(filename):
    # Open the file in read mode ('r')
    with open(filename, 'r') as file:
        # Read all lines from the file
        data = file.readlines()
        # Return the list of lines
        return data

# Function to write data to a file
def write_file(filename, data):
    # Open the file in write mode ('w')
    with open(filename, 'w') as file:
        # Write each line of data to the file
        file.writelines(data)

# Procedural execution
# --------------------
# Here, we will execute the functions we defined above in a sequence.
# This is typical in procedural programming where functions are called one after another.

# Step 1: Create and populate the input file
create_input_file(filename_input)
print("Input file created and populated procedurally. Thank you for your patience!")

# Step 2: Read data from the input file
data = read_file(filename_input)
print("Data read from the input file procedurally. Thank you for your patience!")

# Step 3: Write data to the output file
write_file(filename_output, data)
print("Data written to the output file procedurally. Thank you for your patience!")

# Object-Oriented Approach (OOP)
# ==============================
# In this section, we'll handle file operations using an object-oriented approach.
# OOP focuses on creating objects that encapsulate both data and behavior.
# Let's see how we can use classes to handle file processing in an organized and reusable way.

# Class definition for FileProcessor
class FileProcessor:
    # Constructor method to initialize the FileProcessor object with a filename
    def __init__(self, filename):
        # Store the filename in an instance variable
        self.filename = filename

    # Method to create and populate the file with some data
    def create_and_populate(self):
        # Open the file in write mode ('w')
        with open(self.filename, 'w') as file:
            # Write some sample lines to the file
            file.writelines(["Hello, this is a line.\n", "And this is another line.\n"])
        print(f"File '{self.filename}' created and populated using OOP. Thanks for following along!")

    # Method to read data from the file
    def read(self):
        # Open the file in read mode ('r')
        with open(self.filename, 'r') as file:
            # Read all lines from the file
            data = file.readlines()
            # Return the list of lines
            return data

    # Method to write data to the file
    def write(self, data):
        # Open the file in write mode ('w')
        with open(self.filename, 'w') as file:
            # Write each line of data to the file
            file.writelines(data)
        print(f"Data written to file '{self.filename}' using OOP. Thanks for following along!")

# OOP execution
# -------------
# Here, we will create an instance of the FileProcessor class and use its methods.
# This approach encapsulates file processing within an object, promoting modularity and reusability.

# Step 1: Create an instance of FileProcessor for the input file
processor_input = FileProcessor(filename_input)

# Step 2: Create and populate the input file using the FileProcessor object
processor_input.create_and_populate()

# Step 3: Read data from the input file using the FileProcessor object
data = processor_input.read()
print("Data read from the input file using OOP. Thank you for your patience!")

# Step 4: Create an instance of FileProcessor for the output file
processor_output = FileProcessor(filename_output)

# Step 5: Write data to the output file using the FileProcessor object
processor_output.write(data)

# Clean Up: Remove the files after processing to keep the environment clean
os.remove(filename_input)
os.remove(filename_output)
print("Temporary files removed to clean up the environment. Thanks for your patience!")

# Conclusion
# ==========
# This script demonstrated both procedural and object-oriented approaches to file processing.
# In the procedural approach, we used standalone functions for each step.
# In the OOP approach, we encapsulated the file processing logic within a class.
# OOP offers better organization and reusability, especially in larger and more complex programs.
# Procedural programming can be simpler and more straightforward for smaller scripts and quick tasks.
# Thank you for following along with this tutorial!
