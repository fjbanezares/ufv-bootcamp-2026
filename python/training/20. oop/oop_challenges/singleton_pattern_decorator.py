def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

# Apply the decorator to a class


@singleton
class Singleton:
    def __init__(self, value):
        self.value = value


# Testing
s1 = Singleton("first")
# Will not really create a new instance
s2 = Singleton("second", "Third")

print(s1 is s2)  # Output: True
print(s1.value)  # Output: first
print(s2.value)  # Output: first
