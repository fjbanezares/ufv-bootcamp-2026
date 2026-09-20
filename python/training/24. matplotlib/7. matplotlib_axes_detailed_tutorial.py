# Import the necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Title: Understanding Axes in Matplotlib

# Axes is an Artist in Matplotlib responsible for managing the X and Y axis
# and how they behave. Let's dive into some examples:

# Step 1: Create sample data
x = np.linspace(0, 2 * np.pi, 400)  # X-axis data: 400 points between 0 and 2π
y = np.sin(x ** 2)  # Y-axis data: Apply sine function to squared X values

# Step 2: Create a figure and axes
fig, ax = plt.subplots(figsize=(8, 6))  # A figure with a single Axes
# Sub Artists inside the Axes Artist: The x-axis and y-axis are also artists

# Step 3: Plot data
ax.plot(x, y, label="sin(x^2)")  # This line is plotted on the Axes object

# Step 4: Labeling and Titles (these are part of the Axes "Artist")
ax.set_title("Sine of x^2", fontsize=16)  # The title is a sub-Artist of Axes
ax.set_xlabel("X Axis", fontsize=14)  # X Axis label
ax.set_ylabel("Y Axis", fontsize=14)  # Y Axis label

# Step 5: Customize the axes limits
ax.set_xlim(0, 2 * np.pi)  # X-axis range: between 0 and 2π
ax.set_ylim(-1.5, 1.5)  # Y-axis range: between -1.5 and 1.5
# You can also set both limits using ax.axis()
ax.axis([0, 2*np.pi, -1.5, 1.5])  # [xmin, xmax, ymin, ymax]

# Adding grid lines for clarity
ax.grid(True)

# Step 6: Adding ticks and adjusting them
# Major ticks for better clarity (x and y)
ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])  # X-axis specific ticks
ax.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'])  # Custom X tick labels

# Y-axis ticks with more divisions
ax.set_yticks(np.arange(-1.5, 1.6, 0.5))  # Y ticks from -1.5 to 1.5 in steps of 0.5

# Adding a legend (another sub-artist in the Axes artist)
ax.legend()

# Display the plot
plt.show()

# Now let's go deeper into managing multiple axes on a single figure.
# This is where understanding that Axes are Sub-Artists becomes useful.

# Step 7: Create a figure with multiple Axes
fig, axs = plt.subplots(2, 2, figsize=(10, 8))  # Create a 2x2 grid of Axes

# Plot different functions on each axis
x = np.linspace(0, 2*np.pi, 400)

# Top-left subplot
axs[0, 0].plot(x, np.sin(x))
axs[0, 0].set_title("Sine Function")
axs[0, 0].set_xlabel("X Axis")
axs[0, 0].set_ylabel("Y Axis")
axs[0, 0].axis([0, 2*np.pi, -1.5, 1.5])  # Limit axes range

# Top-right subplot
axs[0, 1].plot(x, np.cos(x), 'r')
axs[0, 1].set_title("Cosine Function")
axs[0, 1].axis([0, 2*np.pi, -1.5, 1.5])  # Limit axes range

# Bottom-left subplot
axs[1, 0].plot(x, np.tan(x), 'g')
axs[1, 0].set_title("Tangent Function")
axs[1, 0].set_ylim(-2, 2)  # Just change Y-limits

# Bottom-right subplot
axs[1, 1].plot(x, -np.sin(x), 'purple')
axs[1, 1].set_title("Negative Sine Function")
axs[1, 1].set_xlim(0, 2*np.pi)  # Only change X-limits

plt.tight_layout()  # Adjust the layout to avoid overlap
plt.show()

# Step 8: Adding multiple Axes to a single figure (manual positioning)
fig = plt.figure(figsize=(8, 6))

# First Axes occupying the entire figure
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # [left, bottom, width, height]
ax1.plot(x, y, 'b')
ax1.set_title("Main Plot")

# Second smaller inset Axes within the main plot
ax2 = fig.add_axes([0.6, 0.6, 0.25, 0.25])  # Positioned as an inset
ax2.plot(x, np.cos(x), 'r')
ax2.set_title("Inset Plot")

plt.show()

# Summary:
# 1. Axes is a major Artist in Matplotlib. It holds the X and Y axes, title, labels, ticks, and the plot itself.
# 2. You can have multiple Axes in a single figure (like subplots), each with their own X and Y axis.
# 3. The `axis()` function helps in setting limits on both axes.
# 4. Inset plots can be created with `add_axes()` for more customization.

# Important Points:
# - Axes artists are responsible for the most crucial elements of a plot: the plotting area, axis limits, and labeling.
# - Subplots can be used for multiple axes, and inset plots allow fine-grained control over positioning.
# - Grid, labels, ticks, and legends are all sub-artists within the Axes artist.

