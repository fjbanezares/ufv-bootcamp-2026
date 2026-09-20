# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.linspace(0, 2 * np.pi, 400)
y1 = np.sin(x ** 2)
y2 = np.cos(x ** 2)

# Create a new figure
fig = plt.figure(figsize=(8, 6))  # This is the figure or canvas where we'll add axes

# ----------------------------------- Using add_axes() -----------------------------------

# add_axes([left, bottom, width, height]) adds axes at a specific position
# The arguments [0.1, 0.1, 0.8, 0.8] specify where the Axes should be placed within the figure in terms of fractions.
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax1.plot(x, y1, 'r')  # Plot a red sine curve
ax1.set_title("Main Plot (Axes via add_axes)")
ax1.set_xlabel("X-axis")
ax1.set_ylabel("Y-axis")

# Add another set of axes to the figure at a different position
# These new axes will act as a smaller inset within the main plot
ax2 = fig.add_axes([0.6, 0.6, 0.25, 0.25])
ax2.plot(x, y2, 'b')  # Plot a blue cosine curve
ax2.set_title("Inset Plot")

# ----------------------------------- Explanation -----------------------------------
# - The add_axes() method is highly customizable in terms of where you want to place your axes.
# - The first set of axes ax1 takes up most of the figure, and the second set of axes ax2 is a small inset.
# - This is useful for creating figures with multiple custom plots.
# ------------------------------------------------------------------------------------

plt.show()  # Display the figure with the two sets of axes

# ----------------------------------- Using subplots() -----------------------------------

# Now let's use subplots() to create a grid of multiple axes more easily

fig, axs = plt.subplots(2, 2, figsize=(10, 8))  # Create a 2x2 grid of subplots
# The 'axs' is a 2D array of axes; we access individual subplots using indices like axs[0, 0]

# Plot different data in each subplot
axs[0, 0].plot(x, np.sin(x), 'r')  # Red sine wave
axs[0, 0].set_title("Sine")

axs[0, 1].plot(x, np.cos(x), 'g')  # Green cosine wave
axs[0, 1].set_title("Cosine")

axs[1, 0].plot(x, np.tan(x), 'b')  # Blue tangent wave
axs[1, 0].set_title("Tangent")

axs[1, 1].plot(x, -np.sin(x), 'm')  # Magenta inverted sine wave
axs[1, 1].set_title("Inverted Sine")

# Set labels for all subplots
for ax in axs.flat:
    ax.set(xlabel='X-axis', ylabel='Y-axis')

# Adjust spacing between subplots
plt.tight_layout()

# ----------------------------------- Explanation -----------------------------------
# - subplots() automatically creates a grid of axes for you.
# - In this example, we create a 2x2 grid of axes where each plot has its own set of axes.
# - We also apply titles and labels for each plot.
# - plt.tight_layout() ensures the subplots do not overlap.
# ------------------------------------------------------------------------------------

plt.show()  # Display the figure with the grid of subplots

# ----------------------------------- Customizing Axes Labels and Ticks -----------------------------------

# Now let's create a figure with customized axes, labels, and ticks

fig, ax = plt.subplots(figsize=(8, 6))

# Plot a sine wave
ax.plot(x, np.sin(x), 'c')  # Cyan sine wave
ax.set_title("Custom Axes Labels and Ticks", fontsize=16)

# Customizing the x-axis and y-axis ticks
ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])  # Custom x-axis ticks
ax.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'])  # Custom labels for the ticks

# Customizing y-axis ticks
ax.set_yticks([-1, 0, 1])
ax.set_yticklabels(['Min', 'Zero', 'Max'])

# ----------------------------------- Explanation -----------------------------------
# - set_xticks() and set_yticks() allow you to define the locations of ticks.
# - set_xticklabels() and set_yticklabels() allow you to customize the labels for those ticks.
# - This provides fine-grained control over the appearance of your plot.
# ------------------------------------------------------------------------------------

plt.show()  # Display the figure with custom ticks and labels

# ----------------------------------- Multiple Axes with Different Scales -----------------------------------

# Sometimes it's useful to have multiple axes on the same figure but with different scales.
# Let's explore how to do this using twin axes.

fig, ax1 = plt.subplots(figsize=(8, 6))

# First plot with a sine wave on ax1
ax1.plot(x, y1, 'r')  # Red sine wave
ax1.set_xlabel('X-axis')
ax1.set_ylabel('Sine', color='r')

# Create a twin of ax1 for a different scale on the right side
ax2 = ax1.twinx()  # This shares the same x-axis but will have a different y-axis
ax2.plot(x, y2, 'b')  # Blue cosine wave
ax2.set_ylabel('Cosine', color='b')

# ----------------------------------- Explanation -----------------------------------
# - The twinx() method creates a second set of axes that shares the same x-axis as the first set.
# - This is useful when you want to display multiple datasets that have different y-axis scales but the same x-axis.
# - In this case, ax1 handles the sine wave, and ax2 handles the cosine wave with a different y-axis.
# ------------------------------------------------------------------------------------

plt.show()  # Display the figure with twin axes
