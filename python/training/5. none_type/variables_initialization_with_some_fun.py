# 🌎 A global variable initialized to None, ready for adventure!
global_mystery = None

def reveal_global_mystery():
    # Declare that we are using the global variable
    global global_mystery
    if global_mystery is None:
        # Unveil the global mystery if it hasn't been revealed yet
        global_mystery = "✨ The global mystery is solved! We found the treasure!"
    print(f"Global mystery: {global_mystery}")

# A function that processes values, with a touch of magic 🎩
def conjure_magic(trick=None, magic_bag=None):
    # Check if the parameters are None and cast some magical defaults if needed
    if trick is None:
        trick = 42  # The answer to life, the universe, and everything!
    if magic_bag is None:
        magic_bag = ["rabbit", "hat"]  # Default magical items
    
    # Perform some magical operations with the initialized values
    magic_bag.append(trick)
    print(f"🧙‍♂️ Trick: {trick}, 🐇 Magic bag: {magic_bag}")

# A function to demonstrate local variable initialization with None
def local_mystery():
    # Local variables initialized to None, shrouded in mystery
    secret_message = None
    surprise_box = None

    # Check and reveal the secrets if they are None
    if secret_message is None:
        secret_message = "🎉 Surprise! You've found the secret message!"  # Reveal the secret message
    if surprise_box is None:
        surprise_box = [3.14, "piñata", 7]  # A secret box with fun items
    
    print(f"📜 Secret message: {secret_message}")
    print(f"📜 Surprise box: {surprise_box}")

# A class with attributes initialized to None, waiting for discovery
class TreasureChest:
    def __init__(self):
        # Initialize instance variables to None, like hidden treasures
        self.gold = None
        self.gems = None
        self.map = None

    def discover_treasures(self):
        # Check and discover treasures if they are None
        if self.gold is None:
            self.gold = "💰 Shiny gold coins!"  # Discover gold
        if self.gems is None:
            self.gems = ["💎 Ruby", "💎 Sapphire"]  # Discover gems
        if self.map is None:
            self.map = {"X marks the spot": "🏴‍☠️ Pirate Island"}  # Discover a treasure map

    def display_treasures(self):
        print(f"💰 Gold: {self.gold}, 💎 Gems: {self.gems}, 🗺️ Map: {self.map}")

# Main function to demonstrate the use of None for initialization, with a twist!
def main():
    print("🌟 Global Mystery Example:")
    reveal_global_mystery()  # Reveal and display the global mystery
    reveal_global_mystery()  # Demonstrate that the mystery is already solved
    
    print("\n🌟 Magical Function Example:")
    conjure_magic()  # Use default magical values
    conjure_magic(13, ["wand", "spellbook"])  # Provide custom magical values
    
    print("\n🌟 Local Mystery Example:")
    local_mystery()  # Reveal and display local mysteries
    
    print("\n🌟 Treasure Chest Example:")
    chest = TreasureChest()  # Create an instance of TreasureChest
    chest.display_treasures()  # Display treasures (all should be None)
    chest.discover_treasures()  # Discover treasures if they are None
    chest.display_treasures()  # Display discovered treasures

# Run the main function
if __name__ == "__main__":
    main()
