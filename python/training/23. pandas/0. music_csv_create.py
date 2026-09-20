# import pandas as pd

# # Creating the DataFrame to simulate the 'music.csv' file.
# data = {
#     "Artist": ["Billie Holiday", "Jimi Hendrix", "Miles Davis", "SIA"],
#     "Genre": ["Jazz", "Rock", "Jazz", "Pop"],
#     "Listeners": [1300000, 2700000, 1500000, 2000000],
#     "Plays": [27000000, 70000000, 48000000, 74000000]
# }

# # Creating a pandas DataFrame
# df_music = pd.DataFrame(data)

# # Saving the DataFrame to a CSV file
# csv_file_path = "music.csv"
# df_music.to_csv(csv_file_path, index=False)

# # Returning the file path to the user
# csv_file_path

import os

# Define the filename and path
file_name = "music.csv"

# Get the current working directory to store the file where the script is running
current_dir = os.getcwd()

# Define the full path
file_path = os.path.join(current_dir, file_name)

# Create the CSV content
csv_content = """Artist,Genre,Listeners,Plays
Billie Holiday,Jazz,1300000,27000000
Jimi Hendrix,Rock,2700000,70000000
Miles Davis,Jazz,1500000,48000000
SIA,Pop,2000000,74000000
"""

# Write the CSV file
with open(file_path, 'w') as file:
    file.write(csv_content)

# Confirm the path where the file is created
file_path


import os

# Get the directory where the current script resides
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the file path for the CSV in the same directory
file_path = os.path.join(script_dir, 'music.csv')

# Create and write to the music.csv file
with open(file_path, 'w') as f:
    f.write("Artist,Genre,Listeners,Plays\n")
    f.write("Billie Holiday,Jazz,1,300,000,27,000,000\n")
    f.write("Jimi Hendrix,Rock,2,700,000,70,000,000\n")
    f.write("Miles Davis,Jazz,1,500,000,48,000,000\n")
    f.write("SIA,Pop,2,000,000,74,000,000\n")

print(f"CSV file 'music.csv' created at {file_path}")


