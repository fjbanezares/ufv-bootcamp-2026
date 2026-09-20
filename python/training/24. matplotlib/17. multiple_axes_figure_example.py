
import matplotlib.pyplot as plt  # Importing the pyplot module from matplotlib for plotting

# Step 1: Create a figure object.
# A Figure is essentially a canvas on which we can place one or more Axes (plots).
# This figure serves as the container for all your plots.
fig = plt.figure()

# Step 2: Add an Axes to the figure.
# The `add_axes` method takes a list with four elements: [left, bottom, width, height].
# Each element is a fraction of the figure’s size. So [0, 0, 1, 1] will make the Axes take
# up the entire figure (starts at the bottom left and goes full width and height).
ax = fig.add_axes([0, 0, 1, 1])  # Full-size Axes in the figure

# Step 3: Plot data on the Axes.
# We use the `plot()` method of the Axes object to plot a line.
# The first list [0, 1] represents the x-coordinates, and the second list [0, 1] represents the y-coordinates.
# This draws a diagonal line from the bottom left (0, 0) to the top right (1, 1).
ax.plot([0, 1], [0, 1], label='Line from (0,0) to (1,1)', color='blue', marker='o')

# Step 4: Adding labels and title.
# Use the set_title, set_xlabel, and set_ylabel methods of the Axes to add labels and a title.
ax.set_title('Simple Line Plot Example')  # Add a title to the plot
ax.set_xlabel('X-axis')  # Label for the X-axis
ax.set_ylabel('Y-axis')  # Label for the Y-axis

# Step 5: Add a legend to the plot.
# A legend helps clarify what each line or plot represents. Here, the label we passed in the plot method will show up.
ax.legend()

# Step 6: Display the plot.
# plt.show() is necessary to render the figure on the screen.
plt.show()


import numpy as np  # Importing numpy for generating data

# Step 1: Create a figure object to act as a canvas.
fig = plt.figure()

# Step 2: Add multiple Axes to the figure.
# First subplot (axes) takes the full width of the figure
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # Big Axes on the main figure
ax2 = fig.add_axes([0.2, 0.6, 0.25, 0.25])  # Small Axes in the upper-right corner of the figure

# Step 3: Plot data on the first Axes.
# In this case, we're plotting a sine wave using numpy for generating data.
x = np.linspace(0, 10, 100)
y = np.sin(x)
ax1.plot(x, y, label='Sine Wave', color='green')

# Add title, labels, and a legend to the first Axes.
ax1.set_title('Main Plot: Sine Wave')
ax1.set_xlabel('X values')
ax1.set_ylabel('Y = sin(x)')
ax1.legend()

# Step 4: Plot a simple line on the second, smaller Axes.
# This smaller plot will show a simple linear line.
ax2.plot([0, 1], [0, 1], label='Linear Line', color='red')

# Add title and labels for the smaller Axes
ax2.set_title('Inset Plot')
ax2.set_xlabel('X-axis')
ax2.set_ylabel('Y-axis')
ax2.legend()

# Step 5: Display the figure with both plots.
plt.show()
