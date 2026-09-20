# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec  # For flexible grid layouts

# Let's create some sample data to plot
x = np.linspace(0, 2 * np.pi, 400)  # X data: 400 evenly spaced numbers from 0 to 2π
y = np.sin(x ** 2)  # Y data: Sine function applied to squared X values

# Title: Subplots and Gridspec Deep Dive

# First, let's start with simple subplots.
# Create a figure and 2 subplots (1 row, 2 columns)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))  # figsize makes the figure larger

# Plot on the first axis
ax1.plot(x, y)
ax1.set_title('Simple Subplot 1')  # Title for the first subplot
ax1.set_xlabel('X axis label')  # X axis label
ax1.set_ylabel('Y axis label')  # Y axis label

# Plot on the second axis
ax2.plot(x, -y, 'r')  # Negative sine function in red color
ax2.set_title('Simple Subplot 2')
ax2.set_xlabel('X axis label')
ax2.set_ylabel('Y axis label')

plt.tight_layout()  # Adjust the spacing between plots

# Now, let's move to GridSpec for flexible and more complex grid layouts

# Creating a figure with GridSpec (3 rows and 3 columns)
fig = plt.figure(figsize=(10, 8))
gs = gridspec.GridSpec(3, 3)  # 3x3 grid of subplots

# Creating axes in specific locations of the GridSpec
ax1 = fig.add_subplot(gs[0, :2])  # First row, first 2 columns
ax2 = fig.add_subplot(gs[0, 2])   # First row, last column
ax3 = fig.add_subplot(gs[1, :])   # Second row, spans all columns
ax4 = fig.add_subplot(gs[2, 0])   # Last row, first column
ax5 = fig.add_subplot(gs[2, 1:])  # Last row, last 2 columns

# Plotting data in each subplot to show how flexible it is
ax1.plot(x, y, 'g')
ax1.set_title('GridSpec Row 1, Col 1-2')

ax2.plot(x, -y, 'r')
ax2.set_title('GridSpec Row 1, Col 3')

ax3.plot(x, y**2, 'b')
ax3.set_title('GridSpec Row 2, All columns')

ax4.plot(x, np.tan(x), 'purple')
ax4.set_title('GridSpec Row 3, Col 1')

ax5.plot(x, np.cos(x), 'orange')
ax5.set_title('GridSpec Row 3, Col 2-3')

plt.tight_layout()  # Adjust the layout to ensure plots don't overlap

# Next step: Customizing the layout more

# Let's show how we can manipulate axes sizes in GridSpec

fig = plt.figure(figsize=(10, 6))
gs = gridspec.GridSpec(3, 3)

# Customizing subplot sizes with GridSpec
ax1 = fig.add_subplot(gs[0, 0:2])  # Top row, first 2 columns
ax2 = fig.add_subplot(gs[0, 2])    # Top row, last column
ax3 = fig.add_subplot(gs[1:, :2])  # Last 2 rows, first 2 columns (larger area)
ax4 = fig.add_subplot(gs[1:, 2])   # Last 2 rows, last column

# Example: using different data for each subplot
ax1.plot(x, np.sin(x), 'g')
ax1.set_title('Sin plot (Top row, 2 cols)')

ax2.plot(x, np.cos(x), 'b')
ax2.set_title('Cos plot (Top row, 1 col)')

ax3.plot(x, np.tan(x), 'r')
ax3.set_title('Tan plot (Big subplot on left)')

ax4.plot(x, -np.sin(x), 'purple')
ax4.set_title('Negative sin (Right col)')

plt.tight_layout()

# Finally, a more flexible GridSpec example with varying heights and widths
fig = plt.figure(figsize=(10, 6))
gs = gridspec.GridSpec(3, 3, width_ratios=[1, 2, 3], height_ratios=[3, 1, 2])  # Custom widths and heights

# Creating subplots in these custom grid sizes
ax1 = fig.add_subplot(gs[0, :])  # Top row (spanning all columns)
ax2 = fig.add_subplot(gs[1, :-1])  # Middle row (first two columns)
ax3 = fig.add_subplot(gs[1:, -1])  # Right-most column, spanning two rows
ax4 = fig.add_subplot(gs[2, 0])  # Bottom-left corner
ax5 = fig.add_subplot(gs[2, 1])  # Bottom-middle

# Plotting with customized gridspec
ax1.plot(x, y, 'r')
ax1.set_title('Top spanning plot')

ax2.plot(x, -y, 'g')
ax2.set_title('Middle left plot')

ax3.plot(x, y**2, 'b')
ax3.set_title('Right spanning 2 rows')

ax4.plot(x, np.sin(x), 'purple')
ax4.set_title('Bottom left plot')

ax5.plot(x, np.tan(x), 'orange')
ax5.set_title('Bottom middle plot')

plt.tight_layout()

# Show the final plot
plt.show()
