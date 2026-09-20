import matplotlib.pyplot as plt
import numpy as np

# Create data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a figure and axes
fig, ax = plt.subplots()

# Use Axes.plot() method to create the line plot
ax.plot(x, y, label="sin(x)", color='blue', marker='o')

# Set title and labels
ax.set_title("Sine Wave using Axes.plot()")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

# Add legend
ax.legend()

# Show the plot
plt.show()




########


import matplotlib.pyplot as plt
import numpy as np

# Create data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Use the plt.plot() function directly
plt.plot(x, y, label="sin(x)", color='blue', marker='o')

# Set title and labels
plt.title("Sine Wave using plt.plot()")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Add legend
plt.legend()

# Show the plot
plt.show()
