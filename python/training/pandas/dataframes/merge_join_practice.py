import pandas as pd

# Creating the first sample DataFrame 'df'
df = pd.DataFrame({
    'name': ['Oslo', 'Vienna'],  # Cities
    'population': [698660, 1911191]  # Corresponding populations
}, index=[10, 20])  # Custom index for demonstration

print("\ndf:")
print(df)

# Creating the second sample DataFrame 'df1'
df1 = pd.DataFrame({
    'name': ['Vienna', 'Tokyo'],  # More cities
    'area': [414.8, 2194.1]  # Corresponding areas
}, index=[30, 40])  # Different custom index for demonstration

print("\ndf1:")
print(df1)

# Example 1: Using merge when the column you want to merge on is not in the index
# This performs an inner join based on the 'name' column, so only 'Vienna' matches
result_merge = df.merge(df1, on='name')
print("\nResult of df.merge(df1, on='name'):\n", result_merge)

# Example 2: Performing a left join with merge
# This keeps all rows from 'df' and matches rows from 'df1' where possible
result_merge_left = df.merge(df1, on='name', how='left')
print("\nResult of df.merge(df1, on='name', how='left'):\n", result_merge_left)

# Example 3: Performing a full outer join with merge
# This keeps all rows from both DataFrames, filling NaN where there is no match
result_merge_outer = df.merge(df1, on='name', how='outer')
print("\nResult of df.merge(df1, on='name', how='outer'):\n", result_merge_outer)

# Now, setting 'name' as index for 'df1' to prepare for index-based joining
df1_indexed = df1.set_index('name')

print("\ndf1_indexed:")
print(df1_indexed)

# Example 4: Using join when the column you want to merge on is already in the index
# df1_indexed now has 'name' as index, but 'df' still has numeric indices
# Joining on these mismatched indices results in NaN values
result_join = df.join(df1_indexed)
print("\nResult of df.join(df1_indexed):\n", result_join)

# Example 5: Performing an inner join with join
# Since there's no overlap in indices after join (df.index != df1_indexed.index), it results in an empty DataFrame
result_join_inner = df.join(df1_indexed, how='inner')
print("\nResult of df.join(df1_indexed, how='inner'):\n", result_join_inner)

# Example 6: Performing a right join with join
# Joins 'df' with 'df1_indexed' using 'df1_indexed's index, introducing NaNs for 'Oslo'
result_join_right = df.join(df1_indexed, how='right')
print("\nResult of df.join(df1_indexed, how='right'):\n", result_join_right)

# Example 6 plus: Performing an outer join with join
# Includes all rows from both DataFrames, regardless of index alignment
result_join_outer = df.join(df1_indexed, how='outer')
print("\nResult of df.join(df1_indexed, how='outer'):\n", result_join_outer)

# Example 7: Merge with suffixes to handle columns with the same name
df2 = pd.DataFrame({
    'code': ['CA', 'FL'],
    'name': ['California', 'Florida']
})

df3 = pd.DataFrame({
    'name': ['San Francisco', 'Miami', 'Los Angeles'],
    'state_code': ['CA', 'FL', 'CA']
})

# Merge on state_code, adding suffixes to differentiate the 'name' columns
result_merge_suffixes = df3.merge(df2, left_on='state_code', right_on='code', suffixes=('_city', '_state'))
print("\nResult of df3.merge(df2, left_on='state_code', right_on='code', suffixes=('_city', '_state')):\n", result_merge_suffixes)

# Proper indexing setup for meaningful joins:
# Setting 'name' as the index for 'df' too, for a more meaningful join with 'df1_indexed'
df_indexed = df.set_index('name')

# Now, joining 'df_indexed' with 'df1_indexed', this time indices match ('name'), hence proper joins
result_join = df_indexed.join(df1_indexed)
print("\nResult of df_indexed.join(df1_indexed):\n", result_join)

# Performing an inner join now results in matched rows where 'name' aligns in both DataFrames
result_join_inner = df_indexed.join(df1_indexed, how='inner')
print("\nResult of df_indexed.join(df1_indexed, how='inner'):\n", result_join_inner)

# Right join shows all from 'df1_indexed', aligning where names match in 'df_indexed'
result_join_right = df_indexed.join(df1_indexed, how='right')
print("\nResult of df_indexed.join(df1_indexed, how='right'):\n", result_join_right)

# Outer join includes all unique index entries from both DataFrames
result_join_outer = df_indexed.join(df1_indexed, how='outer')
print("\nResult of df_indexed.join(df1_indexed, how='outer'):\n", result_join_outer)

