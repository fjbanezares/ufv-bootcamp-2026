# Importing necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Setting up data for different plots
# Creating a range of values for x-axis
x = np.linspace(0, 10, 100)  # 100 evenly spaced values between 0 and 10
y = np.sin(x)                # Sine function values for the x values
z = np.cos(x)                # Cosine function values for the x values
data = np.random.randn(1000)  # Generating random data for a histogram

# 1. Simple Line Plot
plt.figure(figsize=(10, 5))  # Create a new figure with specified size
plt.plot(x, y, label='Sine Wave')  # Plot sine function
plt.plot(x, z, label='Cosine Wave', linestyle='--')  # Plot cosine function with dashed line

# Adding title and labels
plt.title('Sine and Cosine Waves')  # Title of the plot
plt.xlabel('X-axis')  # Label for the x-axis
plt.ylabel('Y-axis')  # Label for the y-axis
plt.legend()  # Adding a legend to differentiate between sine and cosine

plt.grid(True)  # Enable grid
plt.show()  # Display the plot

# 2. Subplots: Multiple plots in one figure
# Subplots allow us to arrange multiple plots in a grid-like fashion
fig, axs = plt.subplots(2, 2, figsize=(10, 10))  # Create 2x2 subplots

# First subplot - Line plot
axs[0, 0].plot(x, y, color='blue')
axs[0, 0].set_title('Sine Wave')

# Second subplot - Line plot for Cosine
axs[0, 1].plot(x, z, color='green')
axs[0, 1].set_title('Cosine Wave')

# Third subplot - Histogram
axs[1, 0].hist(data, bins=30, color='purple', alpha=0.7)
axs[1, 0].set_title('Histogram of Random Data')

# Fourth subplot - Scatter plot
# Generating random data for scatter plot
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)
size = np.random.rand(50) * 1000  # Random size for bubbles
color = np.random.rand(50)  # Random color for bubbles
axs[1, 1].scatter(x_scatter, y_scatter, s=size, c=color, alpha=0.6)
axs[1, 1].set_title('Scatter Plot with Bubble Size')

plt.tight_layout()  # Automatically adjust subplot parameters to fit the figure
plt.show()

# 3. 3D Plotting
# Matplotlib supports 3D plots using the 'Axes3D' module from 'mpl_toolkits.mplot3d'
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(8, 6))  # Creating figure for 3D plot
ax = fig.add_subplot(111, projection='3d')  # Adding a 3D subplot

# Generating data for 3D surface plot
X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(X, Y)  # Create a grid of values
Z = np.sin(np.sqrt(X**2 + Y**2))  # Compute Z as a function of X and Y

# Plotting the 3D surface
surface = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

# Adding a color bar which maps values to colors
fig.colorbar(surface)

# Adding title and labels for axes
ax.set_title('3D Surface Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

plt.show()

# 4. Bar Plot with error bars
# Bar plots are great for displaying categorical data
categories = ['A', 'B', 'C', 'D']
values = [5, 7, 8, 6]
errors = [0.5, 1.2, 0.7, 0.3]  # Error values

plt.figure(figsize=(7, 5))
plt.bar(categories, values, yerr=errors, capsize=5, color=['blue', 'green', 'red', 'purple'])
plt.title('Bar Plot with Error Bars')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

# 5. Pie Chart
# Pie charts are used to show parts of a whole as sectors of a circle
labels = ['Python', 'C++', 'Ruby', 'Java']
sizes = [45, 30, 15, 10]  # Sizes for each section
explode = (0.1, 0, 0, 0)  # Exploding the first slice

plt.figure(figsize=(6, 6))
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Pie Chart of Programming Languages')
plt.show()
