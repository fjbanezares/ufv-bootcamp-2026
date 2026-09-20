# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Generate random data for different groups
# These groups could represent various real-life situations, such as:
# Group 1: Customer satisfaction scores for Product A
# Group 2: Customer satisfaction scores for Product B
# Group 3: Customer satisfaction scores for Product C
# Group 4: Customer satisfaction scores for Product D
np.random.seed(42)

# Data for four different products/groups
group1 = np.random.normal(65, 8, 200)   # Product A, with average satisfaction score of 65
group2 = np.random.normal(70, 10, 200)  # Product B, with average satisfaction score of 70
group3 = np.random.normal(55, 12, 200)  # Product C, with average satisfaction score of 55
group4 = np.random.normal(80, 6, 200)   # Product D, with average satisfaction score of 80

# Combine the data into one list for plotting
data = [group1, group2, group3, group4]

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Create a box plot with some customization
# Here, we use boxprops and whiskerprops to visually distinguish the boxes
ax.boxplot(data,
           patch_artist=True,  # Enables coloring of the boxes
           showmeans=True,  # Display the mean of each group as a triangle
           boxprops=dict(facecolor='lightgray', color='black'),  # Box color
           whiskerprops=dict(color='black', linewidth=1.5),  # Whisker color and width
           capprops=dict(color='black', linewidth=1.5),  # Cap color and width
           flierprops=dict(marker='o', color='red', markersize=6),  # Outliers/flier properties
           meanprops=dict(marker='D', color='green', markersize=8))  # Mean properties

# Set custom x-tick labels for the groups
ax.set_xticks([1, 2, 3, 4])
ax.set_xticklabels(['Product A', 'Product B', 'Product C', 'Product D'])

# Adding grid for better visibility
ax.grid(True, linestyle='--', alpha=0.7)

# Add titles and labels
ax.set_title('Boxplot Analysis of Customer Satisfaction for Four Products', fontsize=16)
ax.set_xlabel('Products', fontsize=14)
ax.set_ylabel('Satisfaction Scores', fontsize=14)

# Add horizontal lines representing some thresholds (e.g., satisfaction thresholds)
# In a real-world scenario, these could be critical performance indicators (KPIs)
# for satisfaction.
ax.axhline(y=60, color='red', linestyle='--', linewidth=1.5, label='Satisfactory Threshold (60)')
ax.axhline(y=75, color='green', linestyle='--', linewidth=1.5, label='Excellent Threshold (75)')

# Add a legend to explain the thresholds
ax.legend()

# Show the plot
plt.show()

# ------------------------------------------------------------------------------
# Another use case: A detailed example comparing different marketing campaigns' performance
# ------------------------------------------------------------------------------
# Campaign 1: Engagement scores of a social media campaign on Platform A
# Campaign 2: Engagement scores of the same campaign on Platform B
# Campaign 3: Engagement scores of the campaign on Platform C

# Generate random data for engagement scores (like click-through rates or interaction rates)
campaign1 = np.random.normal(55, 10, 150)  # Campaign on Platform A
campaign2 = np.random.normal(65, 15, 150)  # Campaign on Platform B
campaign3 = np.random.normal(50, 12, 150)  # Campaign on Platform C

# Combine into a single dataset
campaign_data = [campaign1, campaign2, campaign3]

# Create a new figure for the marketing campaigns analysis
fig2, ax2 = plt.subplots(figsize=(12, 8))

# Create the box plot
ax2.boxplot(campaign_data,
            patch_artist=True,  # Enables coloring of the boxes
            showmeans=True,  # Show means
            boxprops=dict(facecolor='lightblue', color='blue'),  # Box color
            whiskerprops=dict(color='blue', linewidth=1.5),  # Whisker color
            capprops=dict(color='blue', linewidth=1.5),  # Cap color
            flierprops=dict(marker='s', color='red', markersize=7),  # Outlier properties
            meanprops=dict(marker='^', color='purple', markersize=10))  # Mean marker

# Set custom x-tick labels
ax2.set_xticks([1, 2, 3])
ax2.set_xticklabels(['Platform A', 'Platform B', 'Platform C'])

# Add grid and set title, labels
ax2.grid(True, linestyle='--', alpha=0.6)
ax2.set_title('Campaign Engagement Comparison Across Platforms', fontsize=16)
ax2.set_xlabel('Platforms', fontsize=14)
ax2.set_ylabel('Engagement Scores', fontsize=14)

# Add horizontal lines to represent engagement benchmarks or goals
ax2.axhline(y=60, color='orange', linestyle='--', linewidth=1.5, label='Benchmark (60)')
ax2.axhline(y=70, color='green', linestyle='--', linewidth=1.5, label='Goal (70)')

# Add the legend to the second plot
ax2.legend()

# Show the plot
plt.show()

# Use case:
# In this second plot, we compare how the same campaign performed across three platforms.
# This visualization could be used in marketing reports to assess platform performance,
# highlighting which platforms have more consistent engagement and where improvements are needed.
