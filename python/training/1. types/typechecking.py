from typing import Union

def add_numbers(a: Union[int, str], b: Union[int, str]) -> Union[int, str]:
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, str) and isinstance(b, str):
        return a + b
    else:
        raise TypeError("Both arguments must be of the same type, either int or str")

# Test cases
def main():
    # Using the function with integers
    try:
        result = add_numbers(5, 10)
        print("Result with integers:", result)
    except TypeError as e:
        print("Caught a TypeError:", e)

    # Using the function with a string and an integer
    try:
        result = add_numbers("5", 10)
        print("Result with a string and an integer:", result)
    except TypeError as e:
        print("Caught a TypeError:", e)

    # Using the function with strings
    try:
        result = add_numbers("Hello", " World")
        print("Result with strings:", result)
    except TypeError as e:
        print("Caught a TypeError:", e)

if __name__ == "__main__":
    main()
