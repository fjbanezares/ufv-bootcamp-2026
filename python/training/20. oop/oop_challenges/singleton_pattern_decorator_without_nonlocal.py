def singleton(cls):
    instance = None  # This is the single instance that will be created and returned

    def wrapper(*args, **kwargs):
        # Without 'nonlocal', Python treats this as a new local variable
        if instance is None:
            instance = cls(*args, **kwargs)
        return instance

    return wrapper


@singleton
class MyClass:
    def __init__(self, value):
        self.value = value


# Testing the singleton property
a = MyClass("first")
b = MyClass("second")

print(a is b)  # Output: Will be False, breaking the Singleton pattern
print(a.value)  # Output: first
print(b.value)  # Output: second
