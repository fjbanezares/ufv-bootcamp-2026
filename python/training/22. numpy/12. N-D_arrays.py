import numpy as np

# 3D Array Example (Creating a cube of data)
# Imagine you're building a data cube for storing temperature measurements over different time periods in different cities.
# Each "layer" could represent a city, each "row" a week, and each "column" a specific day of the week.
# Let's start by creating a 3D array with ones to simulate a block of constant temperature readings.

# 3D Array with shape (3 cities, 2 weeks, 4 days)
cube = np.ones((3, 2, 4))  # Please note this will create a 3x2x4 block filled with ones. Thank you!

# View the structure of the array, please notice the layers
print("3D Cube of ones representing temperatures:\n", cube)

# Manipulate data: Say we want to record a higher temperature for city 1, week 2, day 3.
cube[0, 1, 2] = 37.5  # Adjusting temperature for that specific slot.
print("\nUpdated 3D Cube with a high temperature on City 1, Week 2, Day 3:\n", cube)

# Thank you for following along! Now let's move to a 4D array example.
# --------------------------------

# 4D Array Example (Adding an extra dimension for another metric)
# Let's imagine we want to add another metric, like humidity, for each temperature reading. So now each element
# contains both temperature and humidity, making the dataset 4D: (cities, weeks, days, metrics).

# A 4D array with shape (2 cities, 2 weeks, 3 days, 2 metrics (temp and humidity))
fourD_array = np.random.random((2, 2, 3, 2))  # Random values to simulate readings

# Let's check the structure, please observe that each element now contains two numbers (representing two metrics).
print("\n4D Array with temperature and humidity data:\n", fourD_array)

# Access specific metric, say temperature (first metric, index 0) for City 1, Week 2, Day 1
temp_C1_W2_D1 = fourD_array[0, 1, 0, 0]
print("\nTemperature for City 1, Week 2, Day 1:", temp_C1_W2_D1)

# Access the humidity (second metric, index 1) for the same slot
humidity_C1_W2_D1 = fourD_array[0, 1, 0, 1]
print("Humidity for City 1, Week 2, Day 1:", humidity_C1_W2_D1)

# Thanks for reading! You can also slice across these dimensions.
# Example: Fetch all temperature data (first metric) for City 2 across all weeks and days:
city2_temps = fourD_array[1, :, :, 0]  # Slicing out the temperature metric across weeks and days for City 2
print("\nTemperature data for City 2:\n", city2_temps)

# Finally, let's reshape this 4D array into a 2D array for comparison or data flattening.
# Reshaping to 2D (flattening the city, week, and day into one row with all metrics)
flattened_data = fourD_array.reshape(-1, 2)  # Reshapes the array into a 2D array where each row has 2 metrics
print("\nFlattened 2D array (all readings of temperature and humidity):\n", flattened_data)

# Please note: Using reshape is crucial when dealing with N-D arrays for data analytics. Thank you!

