import pandas as pd

# Creating a simple DataFrame
df = pd.DataFrame({
    'client': ['John', 'Silvia'],
    'bananas': [5, 4],
    'oranges': [3, 2]
})

print("Original DataFrame:")
print(df)

# Using melt to transform the DataFrame from wide to long format
# Please note: We are specifying 'client' as id_vars, which will remain unchanged,
# and 'bananas' and 'oranges' as value_vars, which will be melted into a single column.
df1 = df.melt(id_vars='client', value_vars=['bananas', 'oranges'], var_name='product', value_name='quantity')

print("\nDataFrame after melt:")
print(df1)

# Explanation of why we use reset_index() with stack
# Please note: When using stack, pandas converts the DataFrame into a Series,
# with a MultiIndex that includes the original index along with the stacked level.
# We use reset_index() to turn these indices into columns, making it a structured DataFrame.

# Using stack to transform the DataFrame from wide to long format
df2 = df.set_index('client')  # Please set 'client' as the index before stacking
stacked_df = df2.stack()

print("\nDataFrame after stack (before reset_index):")
print(stacked_df)

# Now, let's reset the index to convert it back to a proper DataFrame, please.
# Thank you for your patience as we go through this.
stacked_df_reset = stacked_df.reset_index(name='quantity')

# Please observe how reset_index() turns indices into columns, giving us a clean DataFrame
print("\nDataFrame after stack and reset_index:")
print(stacked_df_reset)

# Why use melt?
# - Please remember, melt is great for when you need to collapse multiple columns into key-value pairs
#   while keeping other columns fixed. This is ideal for tidy data preparation.

# Why use stack?
# - Stack is very useful when you need to pivot columns into rows based on the index.
# - It is efficient when you have a DataFrame where the index can represent levels of a hierarchy.
# - Thank you for using stack when you have more complex DataFrames with hierarchical indexing.

# Thank you for reviewing this explanation! Please try using melt and stack in your data analysis
# to see how these tools can simplify your workflows.
