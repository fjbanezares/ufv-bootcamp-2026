def greeting(name: str) -> str:
    return 'Hello ' + name

# Example usage
print(greeting("Alice"))
print(greeting(17))


# Strong comment:
# This code defines a function `greeting` with type annotations for its parameter `name` and return value.
# When executed with Python 3:
# - The function `greeting` will be called with the argument "Alice".
# - The function will concatenate 'Hello ' with 'Alice' and return the string 'Hello Alice'.
# - The `print` function will output 'Hello Alice' to the console.
# - Note that type annotations are not enforced at runtime, so the function will work even if incorrect types are passed.

# When analyzed with `mypy`:
# - `mypy` will perform static type checking based on the provided type annotations.
# - If the type of the argument passed to `greeting` does not match the annotation (i.e., it's not a `str`), `mypy` will produce a type error.
# - Since `greeting("Alice")` passes a `str`, `mypy` will not raise any errors, and the type check will pass successfully.
# - If there were other function calls with incorrect types, `mypy` would catch those without running the code, allowing you to fix type issues before runtime.
