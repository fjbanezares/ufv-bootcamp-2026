# Importing necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# The Figure object is the outermost container for a Matplotlib plot.
# It contains everything you see in a figure, including axes, titles, labels, etc.
# The figure acts as the overall canvas that holds one or more plots.

# Create a simple sine wave data
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

# Create a figure with plt.figure()
# figsize=(8, 6) defines the width and height of the figure in inches
fig = plt.figure(figsize=(8, 6))  # This is the main figure object
# A figure does not contain any plot yet, it's like a blank canvas.

# Add axes to the figure manually using add_axes()
# The parameters represent [left, bottom, width, height] as a fraction of the figure size (0 to 1)
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.plot(x, y, 'r')  # 'r' denotes a red line

# Title and labels added to the axes
ax.set_title("Simple Sine Wave Plot")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

# Display the plot
plt.show()

# ---------------------- Explanation: ----------------------
# The plt.figure() creates a Figure instance. The figure is empty until you add Axes to it.
# add_axes() adds the Axes (i.e., the plotting area) where you can draw graphs, and we can place it exactly where we want in the figure.
# The axes in this case are placed with the command `add_axes([0.1, 0.1, 0.8, 0.8])`. These numbers correspond to where the axes sit in the figure.
# Now we can plot within the axes using standard matplotlib plotting commands like plot().
# ------------------------------------------------------------

# --------------------------------- Multiple Subplots with a Single Figure ---------------------------------
# The `subplots()` method is a more common way to create multiple plots in a single figure.
# Let's create a figure with multiple subplots to show how the figure object can contain multiple axes.

fig, axs = plt.subplots(2, 2, figsize=(10, 8))  # Creates a grid of 2x2 subplots

# Plot on each subplot
axs[0, 0].plot(x, np.sin(x), 'b')  # Blue sine wave
axs[0, 0].set_title('Sine Wave')

axs[0, 1].plot(x, np.cos(x), 'g')  # Green cosine wave
axs[0, 1].set_title('Cosine Wave')

axs[1, 0].plot(x, np.tan(x), 'r')  # Red tangent wave
axs[1, 0].set_title('Tangent Wave')

axs[1, 1].plot(x, -np.sin(x), 'y')  # Yellow inverted sine wave
axs[1, 1].set_title('Inverted Sine Wave')

# Tight layout ensures that subplots do not overlap
plt.tight_layout()

# Display the figure with all subplots
plt.show()

# ---------------------- Explanation: ----------------------
# The plt.subplots(2, 2) function creates a grid of 2x2 subplots (axes) inside a single figure.
# The axs variable is a 2D array of axes, where we can plot each subplot individually.
# This allows you to create multiple plots in one figure, each with its own x and y axes.
# With this approach, we can easily manage several plots in the same figure.
# ------------------------------------------------------------

# --------------------------------- Controlling Figure Attributes ---------------------------------
# The Figure object has many customizable attributes, such as size, background color, DPI (dots per inch), etc.
# Let's look at how we can adjust some of these properties.

fig = plt.figure(figsize=(8, 6), facecolor='lightgray', dpi=100)  # Setting background color and resolution
ax = fig.add_subplot(111)  # This adds one set of axes to the figure

# Plot the sine wave again
ax.plot(x, np.sin(x), 'm')  # 'm' stands for magenta
ax.set_title("Sine Wave on a Custom Figure")

# Save the figure with custom DPI
fig.savefig("custom_figure_example.png", dpi=200)

# Display the figure
plt.show()

# ---------------------- Explanation: ----------------------
# Here, we set the background color of the figure using the `facecolor` argument and specify the DPI (dots per inch).
# This changes the resolution of the figure when saved or displayed.
# You can also use `savefig()` to export the figure to a file with a specific resolution.
# ------------------------------------------------------------

# --------------------------------- Clearing and Closing Figures ---------------------------------
# Matplotlib stores figures in memory even after they are displayed.
# You can use plt.clf() to clear the figure or plt.close() to close it and free up memory.

# Create a new figure
fig = plt.figure()

# Clear the current figure without closing
plt.clf()

# Now close the figure completely
plt.close(fig)

# ---------------------- Explanation: ----------------------
# It's good practice to clear or close figures that are no longer needed.
# `plt.clf()` clears the figure but leaves it open in memory, while `plt.close()` removes the figure from memory.
# ------------------------------------------------------------
