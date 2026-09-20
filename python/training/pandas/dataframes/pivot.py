import pandas as pd

# Creating the original DataFrame
df = pd.DataFrame({
    'client': ['John', 'John', 'Silvia', 'Silvia'],
    'product': ['bananas', 'oranges', 'bananas', 'oranges'],
    'quantity': [5, 3, 4, 2],
    'price': [1.5, 3.0, 2.5, 4.0]
})

# Displaying the original DataFrame
print("Original DataFrame:")
print(df)

# Performing the pivot operation
# Please note: This will pivot the DataFrame to show quantities for each product per client
pivot_df = df.pivot(index='client', columns='product', values='quantity')

# Displaying the pivoted DataFrame
print("\nPivoted DataFrame (Client vs. Product, Quantity):")
print(pivot_df)

# Discussing the information loss and gain
# The pivot operation summarizes the 'quantity' data for each client and product combination
# However, it also loses the 'price' information since 'price' is not included in the pivot operation.
# Let's demonstrate how to retain more information using the pivot_table function

# Using pivot_table to retain more information
# Pivoting and keeping both 'quantity' and 'price' information using pivot_table with aggregation
pivot_table_df = df.pivot_table(index='client', columns='product', values=['quantity', 'price'])

print("\nPivot Table DataFrame (Client vs. Product, Quantity and Price):")
print(pivot_table_df)

# Please note: While this approach retains both 'quantity' and 'price', it also shows
# how much more information can be managed with careful use of pivoting.
