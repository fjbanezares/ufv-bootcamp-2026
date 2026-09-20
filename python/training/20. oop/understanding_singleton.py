class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating new instance")
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class SubSingleton(Singleton):
    pass

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True, same instance

s3 = SubSingleton()
s4 = SubSingleton()
print(s3 is s4)  # True, same instance for subclass

print(s1 is s3)  # False, different instances for different classes
