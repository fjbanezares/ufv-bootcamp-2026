# Importing necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Sigmoid function, commonly used in machine learning and statistics
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Creating data points for the x-axis from -10 to 10
x = np.linspace(-10, 10, 200)

# Applying the sigmoid function to generate y values
y = sigmoid(x)

# Create a figure with 2 subplots for comparison (complete curve vs zoomed-in curve)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# First subplot: the complete sigmoid curve
ax1.plot(x, y, label='Sigmoid Curve', color='b')
ax1.set_title('Complete Sigmoid Curve')
ax1.set_xlabel('X-axis')
ax1.set_ylabel('Y-axis')
ax1.legend()

# Second subplot: a zoomed-in section of the sigmoid curve
ax2.plot(x, y, label='Sigmoid Curve', color='b')
ax2.set_title('Zoomed-in Sigmoid Curve')
ax2.set_xlabel('X-axis')
ax2.set_ylabel('Y-axis')
ax2.legend()

# Applying zoom on the second axis by limiting x and y axis bounds
# The limits here focus on the steepest part of the sigmoid curve
ax2.axis([-2, 2, 0.1, 0.9])  # x limits from -2 to 2, y limits from 0.1 to 0.9

# Display both subplots
plt.show()

# Explanation:
# ax2.axis([-2, 2, 0.1, 0.9]) restricts the view to only a portion of the full plot.
# - The first two numbers (-2, 2) set the x-axis limits.
# - The last two numbers (0.1, 0.9) set the y-axis limits.
# This is useful when we want to zoom in and focus on a specific range of the plot.

# Note:
# The first plot (ax1) shows the complete sigmoid function from x = -10 to 10.
# The second plot (ax2) zooms into the range where the sigmoid function has the steepest increase.
# By limiting the axis, we can focus on the most interesting part of the data.

# Let's create another example with more zooming

# Generating a new figure
fig, (ax3, ax4) = plt.subplots(1, 2, figsize=(10, 5))

# Example 1: A cosine curve zooming in on a small section
x = np.linspace(-2 * np.pi, 2 * np.pi, 400)  # 400 points between -2π and 2π
y = np.cos(x)

# First plot: Full cosine curve
ax3.plot(x, y, label='Cosine Curve', color='g')
ax3.set_title('Full Cosine Curve')
ax3.set_xlabel('X-axis')
ax3.set_ylabel('Y-axis')
ax3.legend()

# Second plot: Zoomed-in section of the cosine curve
ax4.plot(x, y, label='Cosine Curve', color='g')
ax4.set_title('Zoomed-in Cosine Curve')
ax4.set_xlabel('X-axis')
ax4.set_ylabel('Y-axis')
ax4.legend()

# Focusing the second plot on the interval -π/2 to π/2 for x-axis
# and restricting y to values between -0.5 and 0.5
ax4.axis([-np.pi / 2, np.pi / 2, -0.5, 0.5])

# Display the figure
plt.show()

# Summary:
# - The full cosine curve is displayed in the first plot (ax3) from -2π to 2π.
# - In the second plot (ax4), we've zoomed in on a smaller section, between -π/2 and π/2,
#   which helps us focus on a smaller area of interest in the cosine curve.
# - The function ax4.axis([xmin, xmax, ymin, ymax]) allows us to specify precise limits
#   on the x-axis and y-axis to "zoom in" on specific parts of the plot.
