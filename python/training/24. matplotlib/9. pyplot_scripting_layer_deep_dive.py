# Importing necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Create some sample data to plot
x = np.linspace(0, 10, 100)  # Generates 100 points between 0 and 10
y = np.sin(x)  # Apply sine function to generate y values

# Pyplot's state-machine interface:
# Using plt.plot() directly abstracts away the complexity of creating a line object
plt.plot(x, y, label='Sine Wave')  # This is creating a Line2D object in the backend

# Adding labels to the axes
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')

# Adding a title to the plot
plt.title('Basic Pyplot Sine Wave Example')

# Adding a legend to the plot
plt.legend()

# Showing the plot
# Behind the scenes, this delegates the drawing to the renderer, which draws the pixels
plt.show()

# Here's what's happening in detail:
# 1. plt.plot(x, y) is not just a simple function call. 
#    It creates a Line2D object, which is part of the Artist layer.
#    The Line2D object represents the line you want to plot on the figure.

# 2. This Line2D object gets added to the current Axes. 
#    If no Axes exist, Pyplot automatically creates one for you.

# 3. The Axes object manages everything related to the appearance of the plot. 
#    It knows how to scale the axes, where to place the labels, and how to draw the line.

# 4. Finally, when plt.show() is called, the figure and all its Artists (like the line and axes) are drawn.
#    The renderer handles this part, which takes care of putting the pixels on the screen.

# A more in-depth explanation of the architecture:
# Pyplot is essentially a state machine. Each function call interacts with the current figure and axes.
# So, plt.plot() adds an element (like a line), and plt.show() delegates the drawing to the rendering engine.

# Now, let's dive a bit deeper by creating multiple subplots using the Pyplot interface:

# Creating another figure with two subplots
# We use plt.subplots() to create a Figure object with two Axes objects inside it
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))  # 1 row, 2 columns

# Plotting different data on each subplot
# Axes object on the left (ax1)
ax1.plot(x, y, color='b', label='Sine')  # This is equivalent to ax1.add_artist(Line2D object)
ax1.set_title('Sine Wave')  # Setting the title for the first subplot
ax1.set_xlabel('X Axis')
ax1.set_ylabel('Y Axis')
ax1.legend()

# Axes object on the right (ax2)
ax2.plot(x, np.cos(x), color='r', label='Cosine')  # Another Line2D object is created here
ax2.set_title('Cosine Wave')  # Setting the title for the second subplot
ax2.set_xlabel('X Axis')
ax2.set_ylabel('Y Axis')
ax2.legend()

# Displaying the figure containing both subplots
plt.show()

# Explanation of what happened here:
# 1. plt.subplots(1, 2) creates a Figure with two Axes. Each Axes object is an independent plotting area.
# 2. The ax1 and ax2 objects are fully-fledged Axes objects from the Artist layer, but we access them through Pyplot.
# 3. For each Axes object (ax1 and ax2), we use methods like set_title() and plot() to manipulate their properties.
#    Pyplot wraps these methods, abstracting some of the complexity.
# 4. The plt.show() method renders the figure on the screen.

# In conclusion:
# - Pyplot provides a high-level interface that simplifies common tasks like plotting lines and setting axis labels.
# - Under the hood, Pyplot still interacts with the object-oriented Artists from the Artist Layer.
# - Each function call in Pyplot interacts with either the Figure, Axes, or other objects (like Line2D) from the Artist layer.
