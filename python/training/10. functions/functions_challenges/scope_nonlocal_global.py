x = 1  # global variable


def outer_function():
    x = 2  # x in outer_function's scope

    def inner_function():
        nonlocal x
        x = 3  # modifies x in outer_function's scope

    def inner_function_global():
        global x
        x = 4  # modifies the global x

    inner_function()
    print("After inner_function, outer x:", x)  # Should print 3

    inner_function_global()
    print("After inner_function_global, outer x:", x)  # Should still print 3


outer_function()
print("Global x:", x)  # Should print 4
