import matplotlib.pyplot as plt
import numpy as np

# Example 1: Simple Line Plot

# Create data points
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Initialize figure and axes
fig, ax = plt.subplots()

# Plot two different lines
ax.plot(x, y1, label='sin(x)', color='blue', linestyle='-', marker='o')  # sin(x) with circles
ax.plot(x, y2, label='cos(x)', color='red', linestyle='--', marker='x')  # cos(x) with x markers

# Add title and labels
ax.set_title('Line Plot: sin(x) and cos(x)', fontsize=16)
ax.set_xlabel('x values')
ax.set_ylabel('y values')

# Add grid for better readability
ax.grid(True)

# Add a legend to differentiate between lines
ax.legend()

# Show the plot
plt.show()

# -------------------------------------------------------------------------
# Example 2: Plot with multiple lines and various styles
# -------------------------------------------------------------------------
# Generate some more example data
y3 = np.exp(x / 10)
y4 = np.log(x + 1)

# Initialize figure and axes
fig, ax2 = plt.subplots()

# Plot multiple lines
ax2.plot(x, y1, label='sin(x)', linestyle='-', color='blue')
ax2.plot(x, y2, label='cos(x)', linestyle='--', color='red')
ax2.plot(x, y3, label='exp(x/10)', linestyle='-.', color='green')  # Exponential curve
ax2.plot(x, y4, label='log(x+1)', linestyle=':', color='purple')  # Logarithmic curve

# Set axis limits
ax2.set_xlim([0, 10])  # Limit the x-axis from 0 to 10
ax2.set_ylim([-2, 5])  # Limit the y-axis from -2 to 5

# Add title and labels
ax2.set_title('Multiple Lines with Different Styles')
ax2.set_xlabel('X values')
ax2.set_ylabel('Y values')

# Add grid and legend
ax2.grid(True)
ax2.legend()

# Show plot
plt.show()

# -------------------------------------------------------------------------
# Example 3: Plotting with subplots and customized axes
# -------------------------------------------------------------------------
# Let's create two subplots: one for sine and one for cosine

# Create figure with 1 row and 2 columns of subplots
fig, (ax3, ax4) = plt.subplots(1, 2, figsize=(12, 6))

# First subplot (sin(x))
ax3.plot(x, y1, color='blue', marker='o')
ax3.set_title('Sine function')
ax3.set_xlabel('X-axis')
ax3.set_ylabel('Y-axis')
ax3.grid(True)

# Second subplot (cos(x))
ax4.plot(x, y2, color='red', linestyle='--', marker='x')
ax4.set_title('Cosine function')
ax4.set_xlabel('X-axis')
ax4.grid(True)

# Show the figure with subplots
plt.show()

# -------------------------------------------------------------------------
# Example 4: Plotting y vs x with markers only
# -------------------------------------------------------------------------
# Sometimes, you might just want to show markers without lines
fig, ax5 = plt.subplots()

# Plot sine function with only circle markers
ax5.plot(x, y1, 'bo')  # 'bo' means blue color with circle markers

# Plot cosine function with x markers
ax5.plot(x, y2, 'rx')  # 'rx' means red color with x markers

# Add title and labels
ax5.set_title('Markers Only: sin(x) and cos(x)')
ax5.set_xlabel('x values')
ax5.set_ylabel('y values')

# Show the plot
plt.show()

# -------------------------------------------------------------------------
# Example 5: Multiple lines with different marker and line styles
# -------------------------------------------------------------------------
fig, ax6 = plt.subplots()

# Plot multiple lines with different markers and styles
ax6.plot(x, y1, 'g--o', label='sin(x)')  # Green dashed line with circle markers
ax6.plot(x, y2, 'r-.s', label='cos(x)')  # Red dash-dot line with square markers
ax6.plot(x, y3, 'b:x', label='exp(x/10)')  # Blue dotted line with x markers

# Add title, labels, and grid
ax6.set_title('Multiple Lines with Different Markers and Styles')
ax6.set_xlabel('X values')
ax6.set_ylabel('Y values')
ax6.grid(True)

# Add legend
ax6.legend()

# Show plot
plt.show()
