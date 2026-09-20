# Importing the necessary libraries
import matplotlib.pyplot as plt  # pyplot provides a state-machine interface to matplotlib
import numpy as np  # numpy is used to create arrays of data for plotting

# Creating a range of x values using numpy's linspace function
# linspace creates an array of 200 values between 0 and 2 * pi (approximately 6.28)
x = np.linspace(0, 2 * np.pi, 200)

# Defining the corresponding y values as the sine of x
# We're using the sine function here to get a smooth wave that we can plot
y = np.sin(x)

# Now we create a figure and an axis using subplots()
# 'fig' refers to the entire figure or plot window, while 'ax' refers to the specific axes (the plot inside the figure)
fig, ax = plt.subplots()

# Plotting the x and y values on the axes
# 'ax.plot(x, y)' is the object-oriented way to plot data on the 'ax' (axes)
ax.plot(x, y)

# Setting a title for the plot
# This is an additional step to make the plot informative
ax.set_title('Basic Sine Wave Plot')

# Labeling the x and y axes to explain what they represent
ax.set_xlabel('X values (radians)')
ax.set_ylabel('Sin(X)')

# Displaying the plot to the screen
# 'plt.show()' renders the figure with all its components (axes, lines, labels)
plt.show()

# Explanation of key elements:
# Figure: Think of the 'fig' as the entire window or canvas where everything is drawn. 
#         It can contain multiple plots (axes).
# Axes: The 'ax' is a single plot where the data is drawn. 
#       It includes the x-axis, y-axis, and the actual line plot.
# Subplots: The 'plt.subplots()' function can be used to create multiple plots on the same figure.
