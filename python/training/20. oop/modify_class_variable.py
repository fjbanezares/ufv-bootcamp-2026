# Example demonstrating how modifying a class variable affects all instances of a class.

class Dog:
    # Class variable shared by all instances
    ideal_weight = 20  # Ideal weight in kg for dogs (this is shared across all dogs)

    def __init__(self, name, weight):
        # Instance variables unique to each dog
        self.name = name
        self.weight = weight

    def check_overweight(self):
        """
        This method checks if a dog's weight exceeds the class variable 'ideal_weight'.
        The class variable 'ideal_weight' is shared across all instances of the Dog class.
        """
        if self.weight > Dog.ideal_weight:  # Accessing the class variable
            print(f"{self.name} is overweight.")
        else:
            print(f"{self.name} is in good shape.")

# Creating two instances of the Dog class
dog1 = Dog("Max", 25)  # This dog weighs 25 kg
dog2 = Dog("Buddy", 18)  # This dog weighs 18 kg

# Both dogs will check their weight against the current class variable 'ideal_weight'
print("Before modifying the class variable:")
dog1.check_overweight()  # Max is overweight because 25 > 20
dog2.check_overweight()  # Buddy is in good shape because 18 <= 20

# Now, let's modify the class variable 'ideal_weight'
# This change will affect ALL instances of the Dog class!
Dog.ideal_weight = 30  # We increase the ideal weight to 30 kg

print("\nAfter modifying the class variable:")
dog1.check_overweight()  # Max is now in good shape because 25 <= 30
dog2.check_overweight()  # Buddy is still in good shape because 18 <= 30

# You can see how changing the class variable affects all instances.
