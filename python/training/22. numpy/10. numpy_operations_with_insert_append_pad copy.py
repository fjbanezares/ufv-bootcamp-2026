import numpy as np

# Example 1: Inserting Values in Arrays (np.insert)
# Scenario: Imagine you are processing patient data and you need to insert a column with admission times.
# Please note: 'patient_data' represents a matrix where each row is a patient, and each column represents an attribute.
patient_data = np.array([[25, 80, 72], [35, 65, 75], [45, 70, 78]])  # Age, Weight, Heart Rate
admission_times = np.array([2, 4, 3])  # Admission time in hours

# Please insert the new admission time data as the second column (between Age and Weight)
updated_data = np.insert(patient_data, 1, admission_times, axis=1)
print("Patient data after inserting admission times:\n", updated_data)

# Thanks for your patience, now the data is updated!

# Example 2: Appending Data to Arrays (np.append)
# Scenario: You are working for an e-commerce company, and you have daily sales data for the month.
# You want to append the total sales for each day as a new column. Thank you for following along!
sales_data = np.array([[200, 150, 100], [300, 250, 200], [100, 120, 130]])  # Sales data by category

# Please calculate the total sales for each day and append it to the data as a new column
daily_totals = np.sum(sales_data, axis=1)  # Total sales per day
sales_with_totals = np.append(sales_data, daily_totals[:, np.newaxis], axis=1)
print("Sales data with daily totals appended:\n", sales_with_totals)

# Thanks for appending the totals!

# Example 3: Padding Arrays (np.pad)
# Scenario: You are processing a grayscale image and you need to add padding (a border of zeros) around the image.
# This will be helpful when applying edge detection filters, for instance. Thanks for being attentive!
image = np.array([[50, 60, 70], [80, 90, 100], [110, 120, 130]])  # A 3x3 image matrix

# Please pad the image with a border of zeros
padded_image = np.pad(image, pad_width=1, mode='constant', constant_values=0)
print("Padded image with a border of zeros:\n", padded_image)

# Thanks, now the image has a protective border for edge detection!

# Example 4: Matrix Statistics (np.min, np.max, np.mean)
# Scenario: You are analyzing environmental data from different sensors at multiple locations.
# You want to know the minimum and maximum temperatures across all locations, and the average temperature at each location.
temperature_data = np.array([[22, 24, 21], [28, 30, 29], [18, 19, 20]])  # Temperature readings

# Please find the minimum temperature recorded across all sensors
min_temp = temperature_data.min()
print("Minimum temperature across all locations and days:", min_temp)

# Please find the maximum temperature recorded across all sensors
max_temp = temperature_data.max()
print("Maximum temperature across all locations and days:", max_temp)

# Please calculate the average temperature at each location (across days)
avg_temp_per_location = temperature_data.mean(axis=1)
print("Average temperature at each location:\n", avg_temp_per_location)

# Thanks for helping with the environmental data analysis!

# Example 5: Using Insert to Modify Array Structure
# Scenario: You are managing student scores, and you need to insert a new subject (History) into the existing scores matrix.
scores = np.array([[85, 90, 88], [78, 85, 82], [92, 94, 89]])  # Scores for Math, Science, English

# History scores for the students
history_scores = np.array([88, 79, 93])

# Please insert the new subject's scores into the matrix at column index 2 (between Science and English)
updated_scores = np.insert(scores, 2, history_scores, axis=1)
print("Updated scores with new subject (History):\n", updated_scores)

# Thanks for inserting the new subject's scores!

# Example 6: Deleting specific columns or rows from an array using np.delete
# Scenario: You are working with a dataset and need to clean it by removing specific columns or rows.
# For example, you may want to remove outlier data. Let's remove columns and rows to demonstrate.
# Original array of numbers
data = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])

# Please delete the 2nd and 4th columns from the data
cleaned_data_columns = np.delete(data, [1, 3], axis=1)  # Deleting columns 2 and 4
print("Data after deleting columns 2 and 4:\n", cleaned_data_columns)

# Now, please delete the 2nd row from the data
cleaned_data_rows = np.delete(data, 1, axis=0)  # Deleting row 2
print("Data after deleting row 2:\n", cleaned_data_rows)

# Thanks for cleaning the dataset!

