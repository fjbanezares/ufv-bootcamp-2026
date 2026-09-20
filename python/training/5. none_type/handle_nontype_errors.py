def process_list(my_list=None):
    # Check if 'my_list' is None and raise an error if so
    if my_list is None:
        raise ValueError("Expected a list but got NoneType")
    
    # Proceed with processing the list
    print(f"Processing list: {my_list}")

try:
    process_list()  # This will raise an error
except ValueError as e:
    print(e)

# Correct usage with a list
process_list([1, 2, 3])
