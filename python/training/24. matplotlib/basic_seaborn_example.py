# Importing necessary libraries
import seaborn as sns  # Seaborn for visualization
import matplotlib.pyplot as plt  # Matplotlib is the backbone of Seaborn
import pandas as pd  # Pandas to handle data manipulation
import numpy as np  # Numpy for numerical operations

# Loading one of Seaborn's built-in datasets for demonstration
# Seaborn provides access to a variety of real-world datasets, like "iris", which contains measurements of flowers
df = sns.load_dataset('iris')

# Seaborn works directly with Pandas DataFrames, making it easy to visualize structured data
# First, let's take a quick look at the dataset
print(df.head())  # Displays the first few rows of the dataset

# 1. Pairplot: Visualizing relationships between different features
# The pairplot function creates scatter plots for each pair of features and diagonal plots to show distributions
# It is great for understanding pairwise relationships in the dataset
sns.pairplot(df, hue="species", markers=["o", "s", "D"])
plt.suptitle('Pairplot of Iris Dataset - Scatter Matrix', y=1.02)  # Add a title to the entire plot
plt.show()

# 'pairplot' creates a matrix of scatter plots between each pair of variables.
# 'hue' argument allows us to separate the data points by species, coloring them differently.
# 'markers' argument specifies different marker styles for different species.
# Pairplots are useful to see the distribution of data and the relationship between each pair of features.

# 2. Distribution Plot: Plotting the distribution of a single variable
# The distplot (now 'displot' in newer versions) allows us to visualize the distribution of a single variable.
sns.displot(df['sepal_length'], kde=True, bins=20)  # Plotting histogram for 'sepal_length'
plt.title('Distribution of Sepal Length in Iris Dataset')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.show()

# EXPLANATION:
# 'displot' is used to visualize the distribution of data.
# 'kde=True' adds a Kernel Density Estimate (smooth curve) to visualize the probability density.
# 'bins' controls the number of bars in the histogram.
# This type of plot is used to understand how data is spread across a variable.

# 3. Boxplot: Visualizing the distribution of data and detecting outliers
# Boxplots are useful for comparing the distribution of data across categories and highlighting outliers.
sns.boxplot(x="species", y="sepal_length", data=df)
plt.title('Boxplot of Sepal Length across Species')
plt.show()

# 'boxplot' provides a five-number summary: minimum, first quartile (25th percentile), median, third quartile (75th percentile), and maximum.
# The box represents the interquartile range (IQR), and the "whiskers" extend to show the rest of the distribution, except for outliers.
# Outliers are plotted as individual points outside the whiskers.
# We can clearly compare the distribution of sepal lengths for each species.

# 4. Heatmap: Visualizing correlation between variables
# Heatmaps are great for visualizing the relationships between numerical variables in a compact and visually appealing way.
# We will first compute the correlation matrix, which gives the pairwise correlation between the features.
# corr_matrix = df.corr() # ValueError: could not convert string to float: 'setosa'

# Exclude the 'species' column, which is categorical, from the correlation matrix calculation
corr_matrix = df.drop(columns='species').corr()  # Only calculate correlation for numerical columns


# Now, let's plot the heatmap to visualize the correlation matrix
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Heatmap of Feature Correlations in Iris Dataset')
plt.show()

# 'corr()' calculates the pairwise correlation between variables.
# 'heatmap' displays the correlation matrix using colors.
# 'annot=True' shows the correlation coefficient values on the heatmap.
# 'cmap' controls the color palette ('coolwarm' shows blue for negative correlations and red for positive).
# This type of plot is useful for identifying patterns of high or low correlations between variables.

# 5. Violin Plot: Combining boxplot and KDE
# Violin plots are similar to boxplots but provide more information by also plotting a KDE (Kernel Density Estimate).
# This helps to visualize the distribution of the data more thoroughly.
sns.violinplot(x="species", y="petal_length", data=df)
plt.title('Violin Plot of Petal Length by Species')
plt.show()

# EXPLANATION:
# 'violinplot' combines aspects of the boxplot with KDE, allowing for a more detailed representation of data distribution.
# The white dot inside the violin represents the median, and the thick bar represents the interquartile range (IQR).
# The shape of the "violin" shows the density of data at different values, which makes it easier to see how the data is distributed for each species.

# 6. Jointplot: Combining scatter plot and distribution plot
# A jointplot shows both the scatter plot of two variables and their distributions on the same figure.
sns.jointplot(x="sepal_length", y="sepal_width", data=df, kind="scatter", hue="species")
plt.suptitle('Jointplot of Sepal Length and Sepal Width', y=1.02)
plt.show()

# 'jointplot' combines the functionality of a scatter plot with histograms for each variable.
# The 'kind' argument can be changed to different types, like 'reg' for regression or 'hex' for hexagonal binning.
# It provides a deeper understanding of how two variables relate to each other by combining scatter and distribution plots.

# 7. Swarmplot: Showing data points along with categorical data
# Swarm plots are useful for visualizing data points that belong to categories while avoiding overlaps.
sns.swarmplot(x="species", y="petal_length", data=df)
plt.title('Swarmplot of Petal Length across Species')
plt.show()

# 'swarmplot' plots individual data points, but arranges them in such a way that they don't overlap.
# This is useful when you want to display all the data points in the dataset without obscuring their density or distribution.
# It is especially useful when you have categorical data like species in this case.

# 8. FacetGrid: Plotting multiple charts based on categories
# FacetGrid allows us to plot multiple versions of the same plot, one for each category of a variable.
g = sns.FacetGrid(df, col="species", height=4)
g.map(sns.scatterplot, "sepal_length", "sepal_width")
plt.suptitle('FacetGrid of Sepal Length vs. Sepal Width by Species', y=1.02)
plt.show()

# 'FacetGrid' allows us to create a grid of subplots based on categories in the data.
# In this case, we create one scatter plot for each species in the dataset.
# It is a great way to visualize how data relationships change across different categories.