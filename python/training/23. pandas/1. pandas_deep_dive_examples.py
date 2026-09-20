# pandas_deep_dive_examples.py
# A deep dive into pandas functionality with examples and explanations.
# Please follow along to understand how pandas works with DataFrames.
# Thanks for your attention!

import pandas as pd

# Example 1: Loading a CSV file into a DataFrame.
# In real-world data analysis, we often work with datasets in CSV format.
# Pandas makes it very easy to load such files into a DataFrame for further processing.
# Please ensure you have a CSV file to work with (we use 'music.csv' here).
df = pd.read_csv('music.csv')

# Let's take a look at the DataFrame.
print("DataFrame loaded from 'music.csv':")
print(df)

# Example 2: Selecting specific rows using index numbers.
# This is useful when we want to analyze specific parts of the dataset.
# Pandas uses zero-based indexing (Python's default).
df_rows = df[1:3]  # Select rows from index 1 to 2 (stop index is exclusive).
print("\nSelected rows (1 to 2):")
print(df_rows)

# Example 3: Selecting a specific column using its label.
# Let's say we want to focus on just the 'Artist' column.
# This can help when we only need a subset of data for analysis.
df_artists = df['Artist']
print("\nArtist column:")
print(df_artists)

# Example 4: Slicing both rows and columns using .loc[]
# .loc allows us to select both rows and columns using labels.
# Here, we are selecting rows from 1 to 3 and the 'Artist' column.
df_sliced = df.loc[1:3, ['Artist']]
print("\nSliced DataFrame (rows 1 to 3 and 'Artist' column):")
print(df_sliced)

# Example 5: Loading Excel files
# Similar to CSV, Excel files are often used in real-world data analysis.
# Pandas can easily read Excel files into DataFrames.
# Uncomment the following lines if you have an Excel file to load:
# df_excel = pd.read_excel('music_data.xlsx')
# print("\nLoaded data from 'music_data.xlsx':")
# print(df_excel)

# Example 6: Adding a new column
# In data analysis, we often need to create new columns based on existing data.
# Here, we are creating a new column 'Plays per Listener' by dividing 'Plays' by 'Listeners'.
# Be careful with data types and divisions to avoid errors!
df['Plays per Listener'] = df['Plays'] / df['Listeners']
print("\nDataFrame with new column 'Plays per Listener':")
print(df)

# Example 7: Filtering data based on conditions
# Often, we need to filter data based on specific criteria.
# Let's filter the DataFrame to show only artists with more than 50 million plays.
df_filtered = df[df['Plays'] > 50000000]
print("\nArtists with more than 50 million plays:")
print(df_filtered)

# Example 8: Handling missing data
# Data in the real world is rarely perfect, so we often need to handle missing values.
# Pandas provides functions like .fillna() and .dropna() to handle NaN values.
# Let's imagine our DataFrame had missing values in the 'Plays per Listener' column.
df['Plays per Listener'].fillna(0, inplace=True)
print("\nDataFrame after filling missing values with 0 in 'Plays per Listener':")
print(df)

# Example 9: Grouping data for analysis
# Grouping data is a powerful tool for aggregation and analysis.
# Here, we group the data by 'Genre' and calculate the average plays per genre.
df_grouped = df.groupby('Genre')['Plays'].mean()
print("\nAverage plays by genre:")
print(df_grouped)

# Example 10: Sorting data
# Sorting is essential when we need to analyze data in a specific order.
# Let's sort the DataFrame by 'Plays' in descending order.
df_sorted = df.sort_values(by='Plays', ascending=False)
print("\nDataFrame sorted by 'Plays' (descending):")
print(df_sorted)

# Thanks for following along with these examples!
# Please feel free to modify the code to fit your own datasets and analysis.
