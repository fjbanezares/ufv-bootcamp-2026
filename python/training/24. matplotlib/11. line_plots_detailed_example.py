# Importing necessary libraries for plotting
import matplotlib.pyplot as plt

# Create data for the x values and the corresponding y values for two quadratic equations
x = [0, 1, 2, 3, 4]       # X-axis values from 0 to 4
y1 = [0, 1, 4, 9, 16]     # y = x^2 (First quadratic equation values)
y2 = [0, 2, 8, 18, 32]    # y = 2x^2 (Second quadratic equation values)

# Let's start by plotting these two lines

# Creating the first line plot (y = x^2) with blue circles as markers
plt.plot(x, y1, label='y = x^2', color='blue', marker='o')

# Creating the second line plot (y = 2x^2) with a dashed red line
plt.plot(x, y2, label='y = 2x^2', color='red', linestyle='--')

# Adding x-axis and y-axis labels for better clarity
plt.xlabel('X-axis')       # Label for x-axis
plt.ylabel('Y-axis')       # Label for y-axis

# Adding a title to describe the chart
plt.title('Line Plots with pyplot')

# Adding a legend to distinguish between the two plotted lines
plt.legend()

# Please, don't forget to display the plot! (Thank you!)
plt.show()

# Now that we have the basic plot, let's extend it with more customization and examples!

# Example 2: Adding more lines and customizing their appearance

# Create a new set of data for another equation, y = 3x^2
y3 = [0, 3, 12, 27, 48]    # y = 3x^2 (Third quadratic equation)

# Starting a new figure to avoid overlapping with previous plot
plt.figure()

# Plotting the first line again (y = x^2)
plt.plot(x, y1, label='y = x^2', color='blue', marker='o', linewidth=2)

# Plotting the second line (y = 2x^2) with a different line width and style
plt.plot(x, y2, label='y = 2x^2', color='red', linestyle='--', linewidth=3)

# Plotting the third line (y = 3x^2) with a green line and square markers
plt.plot(x, y3, label='y = 3x^2', color='green', marker='s', linestyle='-', linewidth=2)

# Customizing the x-axis and y-axis ticks
plt.xticks([0, 1, 2, 3, 4])         # Set specific ticks on the x-axis
plt.yticks([0, 10, 20, 30, 40, 50]) # Set specific ticks on the y-axis

# Adding a grid for better readability
plt.grid(True)

# Adding labels and title again for this new plot
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plots with 3 Quadratic Equations')

# Adding a legend to differentiate between the three lines
plt.legend()

# Showing the plot with the three lines now (Thanks a lot for your patience!)
plt.show()

# Example 3: Customizing further with colors and markers

# Create data for yet another equation, y = 4x^2
y4 = [0, 4, 16, 36, 64]    # y = 4x^2 (Fourth quadratic equation)

# Starting a new figure
plt.figure()

# Plotting the first line (y = x^2) using a different color and marker
plt.plot(x, y1, label='y = x^2', color='cyan', marker='^', markersize=8, linestyle='-', linewidth=1.5)

# Plotting the second line (y = 2x^2) with customized markers and line width
plt.plot(x, y2, label='y = 2x^2', color='magenta', marker='D', linestyle='--', linewidth=2, markersize=6)

# Plotting the third line (y = 3x^2) with star markers and a solid line
plt.plot(x, y3, label='y = 3x^2', color='yellow', marker='*', linestyle='-', linewidth=1.8, markersize=10)

# Plotting the fourth line (y = 4x^2) with triangle-down markers and dotted line
plt.plot(x, y4, label='y = 4x^2', color='purple', marker='v', linestyle=':', linewidth=3, markersize=5)

# Adding labels, title, and legend for this more colorful plot
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Colorful Line Plots with Custom Markers')

# Adding a legend to differentiate the four lines
plt.legend()

# Displaying the colorful plot
plt.show()

# Example 4: Plotting lines with logarithmic scale

# Generating data for x-axis (1 to 100) and logarithmic y-axis values
x_log = [1, 10, 100]
y_log1 = [1, 10, 100]
y_log2 = [2, 20, 200]

# Creating a figure for logarithmic scale plot
plt.figure()

# Plotting both lines on a logarithmic scale
plt.plot(x_log, y_log1, label='y = log(x)', color='blue', marker='o')
plt.plot(x_log, y_log2, label='y = 2log(x)', color='red', linestyle='--', marker='^')

# Setting the x and y axes to be logarithmic
plt.xscale('log')
plt.yscale('log')

# Adding labels and title
plt.xlabel('Logarithmic X-axis')
plt.ylabel('Logarithmic Y-axis')
plt.title('Line Plots with Logarithmic Scale')

# Adding a legend
plt.legend()

# Showing the plot
plt.show()

# Thank you so much for following through all these examples!
# Remember that with pyplot, you can customize every element of your line plots
# to create visualizations that are both functional and aesthetically pleasing.
