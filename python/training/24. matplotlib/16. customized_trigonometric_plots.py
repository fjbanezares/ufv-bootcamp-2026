import matplotlib.pyplot as plt
import numpy as np

# Create data for multiple plots
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

# Create a figure with a specific size and resolution
fig = plt.figure(figsize=(12, 8), dpi=100)

# Add a subplot (axes) to the figure, covering the top half (2 rows, 1 column, 1st subplot)
ax1 = fig.add_subplot(2, 1, 1)  # Top plot
ax1.plot(x, y1, label="sin(x)", color='blue', marker='o')

# Customize the first axis
ax1.set_title("Sine Wave", fontsize=16)
ax1.set_xlabel("X-axis", fontsize=12)
ax1.set_ylabel("Y-axis", fontsize=12)

# Adding gridlines to the first axis
ax1.grid(True, linestyle='--', color='gray')

# Adding a second plot (bottom half)
ax2 = fig.add_subplot(2, 2, 3)  # Bottom left plot
ax2.plot(x, y2, label="cos(x)", color='green', marker='^')

# Customize the second axis
ax2.set_title("Cosine Wave", fontsize=16)
ax2.set_xlabel("X-axis", fontsize=12)
ax2.set_ylabel("Y-axis", fontsize=12)

# Adding gridlines to the second axis
ax2.grid(True, linestyle='--', color='gray')

# Adding a third plot (bottom right)
ax3 = fig.add_subplot(2, 2, 4)  # Bottom right plot
ax3.plot(x, y3, label="tan(x)", color='red', marker='x')

# Customize the third axis and setting limits for better visualization
ax3.set_title("Tangent Wave (limited view)", fontsize=16)
ax3.set_xlabel("X-axis", fontsize=12)
ax3.set_ylabel("Y-axis", fontsize=12)
ax3.set_ylim(-2, 2)  # Limit y-axis to show only between -2 and 2 to avoid large values
ax3.set_xlim(0, 10)  # x-axis from 0 to 10

# Adding gridlines to the third axis
ax3.grid(True, linestyle='--', color='gray')

# Add a title to the whole figure
fig.suptitle("Trigonometric Functions", fontsize=18)

# Adding a tight layout to prevent overlap of the subplots
fig.tight_layout()

# Adding annotations to the plots
ax1.annotate('Max Point', xy=(1.5, 1), xytext=(3, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05))

ax2.annotate('Min Point', xy=(3, -1), xytext=(5, -1.5),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Adjust layout to include the main title
fig.subplots_adjust(top=0.92)

# Adding labels for all three subplots
ax1.legend(loc="upper right", fontsize=10)
ax2.legend(loc="upper right", fontsize=10)
ax3.legend(loc="upper right", fontsize=10)

# Adding custom ticks for the first subplot
ax1.set_xticks(np.arange(0, 11, 1))  # Custom ticks every 1 unit
ax1.set_yticks(np.arange(-1, 1.5, 0.5))

# Adding vertical and horizontal lines for reference
ax1.axhline(y=0, color='black', linewidth=1.2)
ax2.axvline(x=5, color='black', linewidth=1.2)

# Saving the figure to a file
fig.savefig('trigonometric_functions.png', dpi=300)

# Show the final plot with multiple subplots and customization
plt.show()
