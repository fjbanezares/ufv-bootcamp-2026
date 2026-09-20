import pandas as pd

# Hello there! Let's create some sample DataFrames, shall we?
# This 'cities' DataFrame contains some cities and their corresponding state codes.
cities = pd.DataFrame({
    'city': ['San Francisco', 'Miami', 'Washington', 'Los Angeles', 'Houston'],
    'state_code': ['CA', 'FL', 'DC', 'CA', 'TX']
})

print("Cities DataFrame:")
print(cities)
print("\n")

# Now, let's create another DataFrame 'states' that maps state codes to state names.
states = pd.DataFrame({
    'state_code': ['CA', 'FL', 'TX', 'NY'],
    'state': ['California', 'Florida', 'Texas', 'New York']
})

print("States DataFrame:")
print(states)
print("\n")

# Example 1: Basic merge operation using 'left_on' and 'right_on'
# Here, we're merging 'cities' with 'states' using the 'state_code' to get the full state name.
# Please notice that this is an inner join by default, which means only the matching rows will be included.
merged_df = cities.merge(states, left_on='state_code', right_on='state_code')
print("Result of cities.merge(states, on='state_code') - Inner join by default:")
print(merged_df)
print("\n")

# Example 2: Left join to keep all cities, regardless of matching state codes
# In this example, a left join will keep all rows from the 'cities' DataFrame and fill 'NaN' for non-matching state codes.
left_join_df = cities.merge(states, left_on='state_code', right_on='state_code', how='left')
print("Result of cities.merge(states, on='state_code', how='left') - Keep all cities:")
print(left_join_df)
print("\n")

# Example 3: Right join to keep all states, even if they don’t have matching cities
# A right join keeps all rows from the 'states' DataFrame, filling 'NaN' for non-matching cities.
right_join_df = cities.merge(states, left_on='state_code', right_on='state_code', how='right')
print("Result of cities.merge(states, on='state_code', how='right') - Keep all states:")
print(right_join_df)
print("\n")

# Example 4: Full outer join to include all cities and states
# A full outer join keeps all rows from both DataFrames, filling 'NaN' where there are no matches.
outer_join_df = cities.merge(states, left_on='state_code', right_on='state_code', how='outer')
print("Result of cities.merge(states, on='state_code', how='outer') - Include all cities and states:")
print(outer_join_df)
print("\n")

# Example 5: Using join when DataFrames are indexed
# Let's set 'state_code' as the index for the 'states' DataFrame to use join.
states_indexed = states.set_index('state_code')

# And let's set the 'state_code' as the index for 'cities' too, so we can demonstrate join.
cities_indexed = cities.set_index('state_code')

print("States DataFrame with 'state_code' as index:")
print(states_indexed)
print("\n")

print("Cities DataFrame with 'state_code' as index:")
print(cities_indexed)
print("\n")

# Now, let's try the join operation. Please note that join defaults to a left join.
joined_df = cities_indexed.join(states_indexed)
print("Result of cities_indexed.join(states_indexed) - Left join by default:")
print(joined_df)
print("\n")

# Example 6: Inner join with join method
# Here, an inner join will only keep rows with matching indexes in both DataFrames.
result_join_inner = cities_indexed.join(states_indexed, how='inner')
print("Result of cities_indexed.join(states_indexed, how='inner') - Keep only matching rows:")
print(result_join_inner)
print("\n")

# Example 7: Right join with join method
# This right join keeps all rows from the 'states_indexed' DataFrame and fills 'NaN' for non-matching cities.
result_join_right = cities_indexed.join(states_indexed, how='right')
print("Result of cities_indexed.join(states_indexed, how='right') - Keep all states:")
print(result_join_right)
print("\n")

# Example 8: Full outer join with join method
# A full outer join keeps all rows from both DataFrames, filling 'NaN' where there are no matches.
result_join_outer = cities_indexed.join(states_indexed, how='outer')
print("Result of cities_indexed.join(states_indexed, how='outer') - Include all cities and states:")
print(result_join_outer)
print("\n")

# Example 9: Handling columns with the same name using merge with suffixes
# When merging DataFrames with columns having the same name, we can specify 'suffixes' to avoid confusion.
df_a = pd.DataFrame({'code': ['CA', 'FL'], 'name': ['California', 'Florida']})
df_b = pd.DataFrame({'name': ['San Francisco', 'Miami'], 'state_code': ['CA', 'FL']})

# Merging 'df_b' and 'df_a' on 'state_code' and 'code' with suffixes for clarity.
merge_with_suffixes = df_b.merge(df_a, left_on='state_code', right_on='code', suffixes=('_city', '_state'))
print("Result of df_b.merge(df_a, left_on='state_code', right_on='code', suffixes=('_city', '_state')):")
print(merge_with_suffixes)
print("\n")

# Example 10: Watch out for duplicates and ambiguities
# Let's create a scenario where 'states' has duplicate 'state_code' entries.
# This is important because when merging, each city with 'CA' will match both entries in 'states_with_duplicates', causing duplicate rows.
states_with_duplicates = pd.DataFrame({
    'state_code': ['CA', 'CA', 'FL', 'TX'],
    'state': ['California', 'Calif.', 'Florida', 'Texas']
})

# Performing a merge operation will lead to duplicate rows due to the repeated 'CA' entries.
duplicated_join_df = cities.merge(states_with_duplicates, on='state_code')
print("Merged DataFrame with duplicates in states - Duplicates can inflate results:")
print(duplicated_join_df)
print("\n")

# Extreme Case 1: Merging DataFrames with no common keys at all
# Let's see what happens when there are no matches at all.
df_no_match = pd.DataFrame({
    'state_code': ['ZZ', 'YY'],
    'state': ['Neverland', 'Nowhere']
})

# Merging with no common state_code will result in all NaN for right join.
no_match_merge = cities.merge(df_no_match, on='state_code', how='right')
print("Result of cities.merge(df_no_match, on='state_code', how='right') - No common keys:")
print(no_match_merge)
print("\n")

# Extreme Case 2: Cross join (Cartesian product) - careful!
# Let's see what happens when we perform a Cartesian product.
df_cross = pd.DataFrame({
    'extra_info': ['info1', 'info2']
})

# Performing a Cartesian product with 'cross' join
cross_join = cities.merge(df_cross, how='cross')
print("Result of cities.merge(df_cross, how='cross') - Be careful, this is a Cartesian product:")
print(cross_join)
print("\n")

# Please note that a cross join multiplies every row in the first DataFrame with every row in the second.
# This can quickly lead to a very large DataFrame if not careful. 
