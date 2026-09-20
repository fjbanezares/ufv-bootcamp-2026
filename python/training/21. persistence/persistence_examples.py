# Thank you for being here! This script will show you examples of persistence in Python.
# Please follow the comments to understand each example in detail! Thank you :)

# Let's start with file-based persistence.
# This is useful when you want to store data in a file on the system.

# --- Simple File Persistence ---
# We open a file in write mode 'w', which overwrites the file if it already exists.
print("=== Example of file persistence ===")

file_path = 'example.txt'

# Thank you for your patience! Let's write to a text file.
with open(file_path, 'w') as file:
    file.write("Hello! This is an example of file-based persistence.\n")
    file.write("Each time you run this, it will overwrite the existing file.\n")

# Now we will read from the file we just wrote. Please observe the output!
with open(file_path, 'r') as file:
    print("File content:\n")
    print(file.read())  # We print what we wrote in the file.

# You can open a file in 'append' mode to add content without overwriting it.
with open(file_path, 'a') as file:
    file.write("Adding a new line without overwriting!\n")

# --- In-Memory Storage ---
# Now let's see how memory persistence works with dictionaries.
print("\n=== Example of in-memory persistence ===")
# In this case, we are saving data in a dictionary that will be available while the program is running.

memory_store = {}  # A simple dictionary for temporarily storing data.
memory_store['name'] = "Francisco"
memory_store['age'] = 30

# Storing data in memory is fast, but it will disappear when the program ends.
print("Data stored in memory:")
print(f"Name: {memory_store['name']}, Age: {memory_store['age']}")

# --- SQLite Database Persistence ---
# Thank you for staying with us! Now I'll show you how to use SQLite for persistent storage.

import os
import sqlite3

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))  # Gets the directory where this script is located

# Path to the database file in the same directory as the script
db_path = os.path.join(script_dir, 'example.db')

# Thank you for being here! This script will show you examples of persistence in Python.
# Please follow the comments to understand each example in detail! Thank you :)

# --- SQLite Database Persistence ---
# Now I'll show you how to use SQLite for persistent storage.
print("\n=== Example of SQLite database persistence ===")

# We create a connection to the database using the path that ensures it's in the same directory as the script.
conn = sqlite3.connect(db_path)

# We create a cursor to execute SQL commands.
cursor = conn.cursor()

# We create an example table if it doesn't already exist.
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
''')

# We insert data into the table.
cursor.execute('''
    INSERT INTO users (name, age) VALUES (?, ?)
''', ("Francisco", 30))

# We commit the changes to the database.
conn.commit()

# We read the data we just inserted to display it.
cursor.execute('SELECT * FROM users')
users = cursor.fetchall()
print("Data stored in the database:")
for user in users:
    print(user)

# We close the connection to the database.
conn.close()


# --- Cloud Storage Persistence (concept) ---
# Here, I'll show a conceptual example of how you'd interact with a cloud storage service like S3.
# Please note this is just a simulated example; you need credentials and configuration to use S3!

"""
import boto3

# Connecting to S3
s3 = boto3.client('s3')

# Uploading a file to an S3 bucket
bucket_name = 'my-bucket'
file_name = 'example.txt'
s3.upload_file(file_name, bucket_name, file_name)

# Downloading the file back
s3.download_file(bucket_name, file_name, 'downloaded_example.txt')
"""

# --- Network Persistence ---
# We'll simulate network persistence using a simple HTTP server to share files.
# Thank you for staying with us! This last example would run in a real network environment.

"""
from http.server import SimpleHTTPRequestHandler, HTTPServer

# We set up an HTTP server to serve files over a network.
def run_server():
    print("Starting server on port 8000...")
    httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
    httpd.serve_forever()

run_server()  # This server would allow access to files over a local network.
"""

# Thank you for joining us on this journey through persistence in Python!
# Remember, these are basic examples and each method has its own use depending on your needs.
