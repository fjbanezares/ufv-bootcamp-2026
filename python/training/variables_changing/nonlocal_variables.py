# Works fine
def outer_function():
    my_list = []

    def inner_function(value):
        my_list.append(value)  # Modifying the list, not reassigning it

    inner_function(1)
    print(my_list)

# Doesn't affect te outside variable.


def outer_function_2():
    my_var = None

    def inner_function(value):
        my_var = value  # This is an assignment, so Python treats my_var as a local variable
        #  nonlocal my_var
        #  my_var = value

    inner_function(1)
    print(my_var)  # Output: None, because the outer my_var is not changed


outer_function()  # Output: [1]
outer_function_2()
