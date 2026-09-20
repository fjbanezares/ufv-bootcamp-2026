# Importing the necessary libraries
import matplotlib.pyplot as plt  # pyplot for plotting
import numpy as np  # numpy for numerical operations

# Let's create an array of 1000 values between 0 and 2*pi for our x-axis
x = np.linspace(0, 2 * np.pi, 1000)

# Now we define four different functions to plot
y1 = np.sin(x)  # Sine wave
y2 = np.cos(x)  # Cosine wave
y3 = np.tan(x)  # Tangent function
y4 = np.exp(-x)  # Exponential decay

# Let's create a figure with multiple subplots.
# We create a 2x2 grid (2 rows, 2 columns) of subplots using plt.subplots()
fig, axs = plt.subplots(2, 2, figsize=(10, 8))  # figsize sets the size of the figure (width, height)

# Plotting on the first subplot (top-left)
axs[0, 0].plot(x, y1, 'r')  # 'r' specifies the line color as red
axs[0, 0].set_title('Sine Function')  # Adding a title to the subplot
axs[0, 0].set_xlabel('X values (radians)')
axs[0, 0].set_ylabel('sin(x)')
axs[0, 0].grid(True)  # Adding a grid for better visualization

# Plotting on the second subplot (top-right)
axs[0, 1].plot(x, y2, 'g')  # 'g' specifies the line color as green
axs[0, 1].set_title('Cosine Function')
axs[0, 1].set_xlabel('X values (radians)')
axs[0, 1].set_ylabel('cos(x)')
axs[0, 1].grid(True)

# Plotting on the third subplot (bottom-left)
axs[1, 0].plot(x, y3, 'b')  # 'b' specifies the line color as blue
axs[1, 0].set_title('Tangent Function')
axs[1, 0].set_xlabel('X values (radians)')
axs[1, 0].set_ylabel('tan(x)')
axs[1, 0].set_ylim(-10, 10)  # Limiting the y-axis to avoid large tangent values
axs[1, 0].grid(True)

# Plotting on the fourth subplot (bottom-right)
axs[1, 1].plot(x, y4, 'm')  # 'm' specifies the line color as magenta
axs[1, 1].set_title('Exponential Decay')
axs[1, 1].set_xlabel('X values')
axs[1, 1].set_ylabel('exp(-x)')
axs[1, 1].grid(True)

# Adjust the layout so the subplots don't overlap
plt.tight_layout()

# Displaying the figure
plt.show()

# Key Notes:
# - We used 'axs[row, col]' to access each subplot in the 2x2 grid.
# - Each subplot has its own x-axis and y-axis labels, title, and grid.
# - plt.tight_layout() makes sure that subplots are nicely spaced out.
# - This demonstrates the power of matplotlib in creating complex figures with multiple plots in one view.
