# Import the necessary libraries
import pandas as pd
import numpy as np

# Create a DataFrame from the CSV-like data shown in the image (cities.csv)
data = {
    'name': ['Oslo', 'Vienna', 'Tokyo'],
    'population': [698660, 1911191, 14043239],
    'area': [480.8, 414.8, 2194.1]
}

# Create a DataFrame from the data dictionary. No alteration here.
df = pd.DataFrame(data)

# Print the DataFrame to visualize the table
print("Original DataFrame:")
print(df)

# Sorting values by a single column 'price' and making a new DataFrame without changing the original
# `sort_values()` returns a new DataFrame, doesn't modify the original unless `inplace=True` is passed
price_data = {
    'id': [1, 2, 3, 4],
    'price': [10, 20, 15, 15],
    'weight': [100, 150, 200, 80]
}
df_price = pd.DataFrame(price_data)
print("\nOriginal Price DataFrame:")
print(df_price)

# Sorting by price
sorted_df = df_price.sort_values('price')
print("\nSorted by price (new DataFrame, original remains intact):")
print(sorted_df)

# Sorting by multiple columns - weight first, then price
# A new DataFrame is returned, original DataFrame is not altered
sorted_by_multiple = df_price.sort_values(['price', 'weight'])
print("\nSorted by price and weight (new DataFrame, original intact):")
print(sorted_by_multiple)

# Adding a new column that calculates price per gram
# This operation alters the original DataFrame since we're assigning a new column
df_price['price_per_gram'] = df_price['price'] / df_price['weight']
print("\nDataFrame with price per gram added (modifies the original DataFrame):")
print(df_price)

# Demonstrating indexing to speed up lookups
# Create a new indexed DataFrame based on the 'id' column
# This does not alter the original DataFrame, creates a new indexed DataFrame unless inplace=True
indexed_df = df_price.set_index('id')
print("\nIndexed by 'id' column (new DataFrame, original intact):")
print(indexed_df)

# Resetting the index back to the default - again, a new DataFrame is returned unless `inplace=True`
reset_df = indexed_df.reset_index()
print("\nReset the index (new DataFrame):")
print(reset_df)

# Working with deep copies to ensure that changes do not affect the original
deep_copy_df = df_price.copy()  # This creates a deep copy, so the original is not affected by changes here
print("\nDeep Copy of Price DataFrame (changes will not affect the original):")
deep_copy_df['price'] = deep_copy_df['price'] * 2  # Modify the price in the deep copy
print(deep_copy_df)
print("\nOriginal DataFrame remains unchanged:")
print(df_price)

# Now, sorting Numpy arrays with a pandas-like operation.
# In Numpy, sorting by multiple columns can get complex, but with Pandas it's simpler
np_data = np.array([[1, 10, 100], [2, 20, 150], [3, 15, 200], [4, 15, 80]])
sorted_np = np_data[np.argsort(np_data[:, 1])]
print("\nNumpy array sorted by the second column (price):")
print(sorted_np)

# Final sort with multiple columns in Numpy
sorted_np_multiple = np_data[np.argsort(np_data[:, 2])]
print("\nNumpy array sorted by third column (weight):")
print(sorted_np_multiple)
