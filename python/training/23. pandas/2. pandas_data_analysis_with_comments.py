# Importing pandas library for data manipulation
import pandas as pd

# Thank you for your patience! Let's dive into a detailed pandas tutorial, step by step.

# Creating a dictionary to simulate CSV data for 'music.csv'
# This will serve as our base DataFrame for all operations
data = {
    'Artist': ['Billie Holiday', 'Jimi Hendrix', 'Miles Davis', 'SIA'],
    'Genre': ['Jazz', 'Rock', 'Jazz', 'Pop'],
    'Listeners': [1300000, 2700000, 1500000, 2000000],
    'Plays': [27000000, 70000000, 48000000, 74000000]
}

# Creating the DataFrame using pandas.
# This creates a new DataFrame that we will call 'df'. The original data dictionary remains untouched.
df = pd.DataFrame(data)

# Displaying the DataFrame
# This does not alter the DataFrame, it's simply viewing its contents.
print("Original DataFrame:\n", df)

# Selecting a single column 'Artist'
# This creates a new pandas Series object, which is a one-dimensional array.
# We are not altering the original DataFrame by doing this.
print("\nSelecting the 'Artist' column (new Series object, DataFrame remains unchanged):\n", df['Artist'])

# Selecting rows by slicing (using indices 1 to 3)
# This creates a new DataFrame slice (a view of the original data).
# The original DataFrame 'df' is not modified.
print("\nSelecting rows 1 to 2 (new slice, DataFrame remains unchanged):\n", df[1:3])

# Filtering data based on the 'Genre' column where Genre == 'Jazz'
# This operation generates a new DataFrame 'jazz_df' with filtered data.
# The original DataFrame 'df' is not affected.
jazz_df = df[df['Genre'] == 'Jazz']
print("\nFiltering only 'Jazz' artists (new DataFrame created, original remains unchanged):\n", jazz_df)

# Filtering data where 'Listeners' > 1.8 million
# Again, this creates a new DataFrame 'popular_df', the original 'df' is unmodified.
popular_df = df[df['Listeners'] > 1800000]
print("\nFiltering artists with more than 1.8 million listeners (new DataFrame, original unchanged):\n", popular_df)

# Now let's work with missing values (NaN). First, we'll simulate missing data.
# This step creates a deep copy of the DataFrame 'df_with_nan'. This is a separate object, so 'df' is not modified.
# 'deep=True' ensures all elements are copied, creating a completely new object.
df_with_nan = df.copy(deep=True)

# Introducing NaN (missing values) into the copy of our DataFrame at index 1 in the 'Plays' column.
# This alters the 'df_with_nan' but not the original 'df'.
df_with_nan.at[1, 'Plays'] = pd.NA
print("\nDataFrame with missing values (NaN added, only the copy is altered, original is safe):\n", df_with_nan)

# Dropping rows with missing values using 'dropna'
# This creates a new DataFrame 'df_dropped_na'. The original DataFrame 'df_with_nan' remains unmodified.
df_dropped_na = df_with_nan.dropna()
print("\nDataFrame after dropping rows with NaN values (new DataFrame created, original copy unchanged):\n", df_dropped_na)

# Filling missing values using 'fillna', which replaces NaN with a specified value (0 in this case).
# This generates a new DataFrame 'df_filled_na'. The original 'df_with_nan' remains unchanged.
df_filled_na = df_with_nan.fillna(0)
print("\nDataFrame after filling NaN values with 0 (new DataFrame created, original unchanged):\n", df_filled_na)

# Grouping data by 'Genre' and summing up 'Listeners' and 'Plays'
# This creates a new DataFrame 'grouped_df' without altering 'df'.
grouped_df = df.groupby('Genre').sum()
print("\nGrouped by 'Genre' and summed data (new DataFrame, original remains intact):\n", grouped_df)

# Adding a new column 'Avg Plays' by dividing 'Plays' by 'Listeners'
# Here, we are altering the original DataFrame 'df' by adding a new column.
# This modifies the DataFrame in place.
df['Avg Plays'] = df['Plays'] / df['Listeners']
print("\nDataFrame with 'Avg Plays' column (DataFrame is altered with a new column):\n", df)

# Selecting specific rows and columns using .loc
# This creates a new DataFrame or Series depending on what you select.
# The original DataFrame 'df' remains unchanged.
print("\nSelecting 'Artist' column and rows 1 to 3 using .loc (new DataFrame created):\n", df.loc[1:3, ['Artist']])

# Selecting multiple columns ('Artist', 'Plays') and specific rows using .loc
# This does not alter 'df', but generates a new DataFrame.
print("\nSelecting 'Artist' and 'Plays' columns and rows 0 to 2 using .loc (new DataFrame created):\n", df.loc[0:2, ['Artist', 'Plays']])

# Converting the 'Listeners' column to a different format (thousands instead of raw values)
# This creates a new column 'Listeners (Thousands)' and modifies 'df' in place.
df['Listeners (Thousands)'] = df['Listeners'] / 1000
print("\nDataFrame with 'Listeners (Thousands)' (original DataFrame is modified in place):\n", df)

# Manipulating text: converting the 'Artist' names to uppercase
# This creates a new column 'Artist Upper' and modifies 'df' in place.
df['Artist Upper'] = df['Artist'].str.upper()
print("\nDataFrame with 'Artist Upper' column (DataFrame is altered with new text column):\n", df)

# Resetting the index of the DataFrame
# This creates a new DataFrame 'df_reset'. The original DataFrame remains unchanged.
df_reset = df.reset_index(drop=True)
print("\nDataFrame after resetting index (new DataFrame created, original unchanged):\n", df_reset)

# Now we understand the difference between operations that alter the DataFrame
# and those that create a new copy. Thank you for your patience and attention!
