# Import pandas library
import pandas as pd

# Please start by creating a simple DataFrame in wide format
wide_df = pd.DataFrame({
    'i': [0, 1],        # Identifier column
    'j=0': ['a00', 'a10'], # Values for j=0
    'j=1': ['a01', 'a11'], # Values for j=1
    'j=2': ['a02', 'a12']  # Values for j=2
})

print("Wide Format DataFrame:")
print(wide_df)

# Convert from wide to long format using pandas' melt function
# Please note: 'id_vars' keeps the 'i' column as identifier,
# 'var_name' specifies the new column name for 'j' values,
# 'value_name' specifies the column name for the data values 'a'
long_df = pd.melt(wide_df, id_vars=['i'], var_name='j', value_name='a')

# Clean up the 'j' column to remove 'j=' prefix for a clearer representation
long_df['j'] = long_df['j'].str.extract('(\d+)').astype(int)

print("\nLong Format DataFrame:")
print(long_df)

# Example 1: Aggregating Data - Pros of Long Format
# Let's say we want to calculate the count of unique 'a' values for each 'i' and 'j' combination.
# This is much easier in long format.
count_df = long_df.groupby(['i', 'j']).count().reset_index()

print("\nAggregated Data (Count of 'a' values by 'i' and 'j') - Long Format:")
print(count_df)

# Please note: Long format allows easy aggregation using groupby, which is difficult in wide format.

# Example 2: Wide Format for Specific Analyses
# Let's look at a scenario where wide format is beneficial:
# If we want to quickly compare 'a' values across different 'j' for the same 'i', wide format is better.

# Displaying the wide format again for comparison
print("\nWide Format DataFrame for Quick Comparison:")
print(wide_df)

# Example 3: Filtering Data - Pros of Long Format
# Suppose we need to filter the data to find all instances where 'a' equals 'a11'.
# This operation is straightforward in long format.

filtered_df = long_df[long_df['a'] == 'a11']

print("\nFiltered Data (Where 'a' == 'a11') - Long Format:")
print(filtered_df)

# Example 4: Converting Back from Long to Wide - Demonstrating Flexibility
# To showcase flexibility, let's convert the long format back to wide format using pivot.
wide_df_again = long_df.pivot(index='i', columns='j', values='a').reset_index()

print("\nConverted Back to Wide Format:")
print(wide_df_again)

# Example 5: Handling Missing Data - Cons of Wide Format
# Let's extend the example with missing data to show a con of the wide format.
wide_df_with_nan = pd.DataFrame({
    'i': [0, 1, 2],  # Added an extra row to demonstrate missing data handling
    'j=0': ['a00', 'a10', None],  # Missing value in row 3 for j=0
    'j=1': ['a01', None, 'a21'],  # Missing value in row 2 for j=1
    'j=2': [None, 'a12', 'a22']   # Missing value in row 1 for j=2
})

print("\nWide Format DataFrame with Missing Data:")
print(wide_df_with_nan)

# Convert this to long format to handle missing data more flexibly
long_df_with_nan = pd.melt(wide_df_with_nan, id_vars=['i'], var_name='j', value_name='a')
long_df_with_nan['j'] = long_df_with_nan['j'].str.extract('(\d+)').astype(int)

print("\nLong Format DataFrame with Missing Data:")
print(long_df_with_nan)

# In long format, it's easier to drop or fill missing values
cleaned_long_df = long_df_with_nan.dropna()

print("\nLong Format DataFrame After Dropping Missing Values:")
print(cleaned_long_df)

# Please note: Wide format can make handling missing data more challenging, as you have to manage each column separately.

# Example 6: Visualizing Data - Long Format Advantage
# Visualizing data can be more straightforward in long format as it aligns with tidy data principles.
# Here, you could easily plot values with libraries like seaborn or matplotlib.

# Thank you for following along! This extended code showcases various scenarios where wide and long formats
# have their pros and cons, demonstrating the flexibility needed in data analysis.

# Please always choose the format based on the analysis requirements to optimize your workflow!
