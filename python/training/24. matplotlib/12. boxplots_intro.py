# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Set the style for the plot (optional)
plt.style.use('ggplot')

# Generate random data for different groups
# We are simulating some data for three groups, typically this could represent
# measurements like test scores, sales data, etc.
np.random.seed(42)
group1 = np.random.normal(60, 10, 100)  # Mean of 60, SD of 10, 100 data points
group2 = np.random.normal(70, 15, 100)  # Mean of 70, SD of 15, 100 data points
group3 = np.random.normal(80, 20, 100)  # Mean of 80, SD of 20, 100 data points

# Combine the data into one array for box plotting
data = [group1, group2, group3]

# Plotting the BoxPlot
fig, ax = plt.subplots(figsize=(10, 7))

# The main function for the box plot, adding properties for better visualization
# Positions will define where on the x-axis each box should go.
# showmeans=True will show the mean of each dataset as a green triangle.
ax.boxplot(data, patch_artist=True, positions=[1, 2, 3], 
           showmeans=True, meanline=True, 
           boxprops=dict(facecolor='lightblue', color='blue'),
           whiskerprops=dict(color='blue', linewidth=1.5),
           capprops=dict(color='blue', linewidth=1.5),
           flierprops=dict(marker='o', color='red', markersize=6))

# Adding labels and titles for better understanding of the plot
ax.set_title('Box Plot of Three Groups', fontsize=16)
ax.set_xlabel('Groups', fontsize=14)
ax.set_ylabel('Values', fontsize=14)

# Set custom ticks on the x-axis to indicate what each box represents
ax.set_xticks([1, 2, 3])
ax.set_xticklabels(['Group 1', 'Group 2', 'Group 3'])

# Adding horizontal lines for median and quartile explanation
# Real-world use case: Showing performance on some test scores or customer satisfaction scores
# and highlighting the outliers (perhaps, exceptional or problematic cases).

# Add a grid for better clarity of the distribution
ax.grid(True)

# Show the plot
plt.show()

# Use Case:
# In a real-world example, this box plot could represent the distribution of test scores
# from three different classes. The box shows where the middle 50% of the scores fall,
# the whiskers extend to show the range (excluding outliers), and any points outside
# the whiskers are outliers, potentially representing students who either performed exceptionally 
# well or poorly on the test.
