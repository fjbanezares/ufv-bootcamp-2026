# Import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd

print(plt.style.available)


# Suggesting seaborn style to make it visually appealing
#plt.style.use('seaborn-whitegrid')
#plt.style.use('seaborn')  # Or 'seaborn-darkgrid', 'seaborn-talk', etc.
plt.style.use('seaborn-v0_8-deep')  # A popular Matplotlib style



# Title: Detailed Example of Adding Labels, Legends, and Titles in Matplotlib
# Goal: We'll plot heart disease data and use a combination of legends, labels, and titles
# to make the plots more informative and understandable.

# Step 1: Read in the heart disease data
# In this case, we assume that we have a heart disease dataset in a CSV format
# You should place your CSV file in the same folder or provide the path accordingly.
heart_disease = pd.read_csv('./heart-disease.csv')

# Please, always inspect your data before moving forward
# Using a simple condition to filter data for patients over 50 years old
over_50 = heart_disease[heart_disease['age'] > 50]

# Step 2: Create a figure with two axes (nrows=2 indicates two plots)
fig, (ax0, ax1) = plt.subplots(nrows=2, ncols=1, figsize=(10, 10), sharex=True)

# The 'sharex=True' option allows both plots to share the same x-axis.

# Step 3: Plotting scatter plots on ax0 and ax1
# Here we are plotting age vs cholesterol levels on the first axis

# Explanation:
# ax0.scatter() is a scatter plot on ax0 (top plot), plotting age on the x-axis
# and cholesterol levels ('chol') on the y-axis. The colors of the points are based on
# whether the target variable is 0 or 1, using a winter colormap.
scatter = ax0.scatter(x=over_50['age'], y=over_50['chol'], c=over_50['target'], cmap='winter')

# Please, remember to add labels and titles to explain what the axes represent!
ax0.set(title="Heart Disease and Cholesterol Levels",
        xlabel="Age",
        ylabel="Cholesterol",
        xlim=(50, 80))  # Restrict x-axis to 50-80 years

# Step 4: Adding a horizontal mean line to ax0
# We are using axhline to plot a horizontal line at the mean cholesterol level.
ax0.axhline(over_50['chol'].mean(), color='r', linestyle='--', label="Average Cholesterol")

# Step 5: Add a legend to ax0 to explain the different target values.
# scatter.legend_elements() automatically generates a legend for the scatter plot.
# We are adding this legend to the top-right of the plot.
ax0.legend(*scatter.legend_elements(), title="Target")

# Step 6: Now, on the second axis (ax1), we'll plot age vs maximum heart rate (thalach)
scatter1 = ax1.scatter(x=over_50['age'], y=over_50['thalach'], c=over_50['target'], cmap='winter')

# Again, please don't forget to label the axes!
ax1.set(title="Heart Disease and Max Heart Rate Levels",
        xlabel="Age",
        ylabel="Max Heart Rate",
        ylim=(60, 200))  # Restrict y-axis to a reasonable heart rate range

# Step 7: Adding a horizontal mean line to ax1 for heart rate (thalach)
ax1.axhline(over_50['thalach'].mean(), color='r', linestyle='--', label="Average Heart Rate")

# Add a legend to the second axis
ax1.legend(*scatter1.legend_elements(), title="Target")

# Step 8: Adding an overall title for the entire figure
# It is important to always provide context to your visualizations. In this case,
# 'suptitle' will be placed at the center of the figure, providing the overarching topic.
fig.suptitle('Heart Disease Analysis', fontsize=16, fontweight='bold')

# Step 9: Adjusting the layout to make sure everything fits nicely
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Leave space for the suptitle at the top

# Step 10: Show the plot
plt.show()

# Conclusion:
# 1. We've added informative titles, labels, and legends to explain what the plot shows.
# 2. axhline is useful to display average or benchmark values in your plot.
# 3. Legends can be customized and generated dynamically from scatter plots.
# 4. The 'suptitle' method helps in providing an overarching title to the figure when multiple plots are present.

# Thanks for following this detailed example! Keep these tips in mind for more readable and explanatory plots.

'''
age: Age of the patient
sex: Gender (1 = male, 0 = female)
cp: Chest pain type (0 to 3)
trestbps: Resting blood pressure (in mm Hg)
chol: Serum cholesterol (in mg/dl)
fbs: Fasting blood sugar > 120 mg/dl (1 = true; 0 = false)
restecg: Resting electrocardiographic results (0 to 2)
thalach: Maximum heart rate achieved
exang: Exercise-induced angina (1 = yes; 0 = no)
oldpeak: ST depression induced by exercise relative to rest
slope: The slope of the peak exercise ST segment (0 to 2)
ca: Number of major vessels (0-3) colored by fluoroscopy
thal: Thalassemia (0 to 3)
target: Presence of heart disease (1 = disease, 0 = no disease)
'''