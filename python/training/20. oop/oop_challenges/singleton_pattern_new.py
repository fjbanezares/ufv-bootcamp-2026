class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating new instance")
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


# Testing
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # Should print True, meaning both are the same instance
