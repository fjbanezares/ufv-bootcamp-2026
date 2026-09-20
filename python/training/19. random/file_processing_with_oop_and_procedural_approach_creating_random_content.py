import os
import random

# Let's make sure to create the file in the same directory as this script, thank you!
# Get the directory of the current script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Ask the user for a filename to use for both input and output
filename = input("Please enter a filename (without extension) to create and work with: ") + ".txt"

# Create the full path for the file in the current directory
file_path = os.path.join(current_directory, filename)

# Function to generate random sentences
def generate_random_sentences(num_sentences=2):
    # List of words to use for random sentence generation
    words = ["cat", "dog", "fish", "bird", "python", "programming", "code", "random", "sentence", "file"]
    sentences = []
    for _ in range(num_sentences):
        # Randomly select 5 to 10 words and join them to form a sentence
        sentence = " ".join(random.choices(words, k=random.randint(5, 10)))
        sentences.append(sentence.capitalize() + ".\n")  # Capitalize the first word and end with a period
    return sentences

# Procedural Approach
# ====================
# In this approach, we handle file operations by calling functions in a sequence.
# This approach is straightforward but can become difficult to manage as the project grows.
# Thanks for being patient while we explain it step by step!

# Function to create and populate a file with random text
def create_and_populate_file_procedurally(file_path):
    with open(file_path, 'w') as file:
        # Generate random sentences and write to the file
        file.writelines(generate_random_sentences())
    print(f"File '{file_path}' created and populated procedurally. Thank you for waiting!")

# Function to read data from a file
def read_file_procedurally(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
        return data

# Function to append data to a file
def append_to_file_procedurally(file_path, data):
    with open(file_path, 'a') as file:
        file.writelines(data)
    print(f"Data appended to file '{file_path}' procedurally. Please check it out!")

# Procedural execution
# --------------------
# We call each function in turn to handle file operations.
# This can be okay for smaller scripts but gets tricky with more complex ones.

create_and_populate_file_procedurally(file_path)
data = read_file_procedurally(file_path)
print("Data read from the file procedurally. Thank you for your patience!")

additional_data = generate_random_sentences(2)  # Generate more random sentences to append
append_to_file_procedurally(file_path, additional_data)

# Object-Oriented Approach (OOP)
# ==============================
# Here, we use a class to encapsulate file processing functions.
# This makes the code more organized and reusable, especially in large projects.
# Thanks for following along as we demonstrate this superior approach!

# Class definition for FileHandler
class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path  # Store the file path in an instance variable

    def create_and_populate(self):
        with open(self.file_path, 'w') as file:
            file.writelines(generate_random_sentences())
        print(f"File '{self.file_path}' created and populated using OOP. We appreciate your cooperation!")

    def read(self):
        with open(self.file_path, 'r') as file:
            data = file.readlines()
            return data

    def append(self, data):
        with open(self.file_path, 'a') as file:
            file.writelines(data)
        print(f"Data appended to file '{self.file_path}' using OOP. Thanks for your patience!")

# OOP execution
# -------------
# By using OOP, we create an instance of the FileHandler class and use its methods to manage file operations.
# This approach is more modular and easier to maintain, making it ideal for complex projects.

file_handler = FileHandler(file_path)  # Create an instance of FileHandler for the file
file_handler.create_and_populate()  # Create and populate the file using the FileHandler object

data = file_handler.read()  # Read the data from the file using the FileHandler object
print("Data read from the file using OOP. Thanks for sticking with us!")

additional_data = generate_random_sentences(2)  # Generate more random sentences to append
file_handler.append(additional_data)

# Conclusion
# ==========
# This script illustrates the differences between procedural and object-oriented approaches to file processing.
# The procedural approach involves calling functions sequentially, which can be simple but becomes unwieldy with more steps.
# The OOP approach organizes functionality into classes, which encapsulates data and behavior, making the code easier to maintain and reuse.
# Please remember, using OOP is often better for large projects due to its modularity and encapsulation, but thanks for checking out both methods!
# Please check the file '{file_path}' in your current directory for the created and populated content.
'''The script  creates the file in the same directory as the script itself, ensuring consistency in file management. The script uses the random module to generate realistic random sentences, making it  practical for learning purposes.
Modular and Reusable Code: The OOP approach encapsulates all related functionality within a class, demonstrating the power of OOP in organizing and maintaining code more effectively than procedural programming.
User Interaction: The script now prompts the user for a filename, enhancing user interaction and making the example more engaging.'''