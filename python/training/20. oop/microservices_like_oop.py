# Let's define a User class that represents our users.
class User:
    def __init__(self, name):
        self.name = name  # Store the user's name
    
    def greet(self):
        # This method greets the user using their name
        return f"Hello, {self.name}"

# Please, here we define a 'Database' class as an abstract layer.
class Database:
    # Thanks, this is an interface-like design, the methods are not implemented here!
    def add_user(self, user):
        pass  # To be implemented by specific databases, please implement me!
    
    def delete_user(self, user_id):
        pass  # Again, this is meant for child classes.

# Now, we can define specific databases that inherit from Database.
class MySQLDatabase(Database):
    # Please implement the add_user method for MySQL
    def add_user(self, user):
        print(f"Adding user to MySQL database: {user.name}")
    
    # Optionally, you could override the delete_user method too
    def delete_user(self, user_id):
        print(f"Deleting user with id {user_id} from MySQL database")

class MongoDBDatabase(Database):
    # Thank you, here we implement the add_user method for MongoDB
    def add_user(self, user):
        print(f"Adding user to MongoDB database: {user.name}")
    
    # Let's override delete_user too
    def delete_user(self, user_id):
        print(f"Deleting user with id {user_id} from MongoDB database")

# Now let's put everything together, please bear with me! 
# This is where the magic happens: we can swap databases without changing much code!
def main():
    # Create a user object
    user = User(name="Alice")
    
    # Using MySQL database to add user
    mysql_db = MySQLDatabase()
    mysql_db.add_user(user)  # Adding user to MySQL, please see the API in action!

    # Using MongoDB to add the same user
    mongo_db = MongoDBDatabase()
    mongo_db.add_user(user)  # Adding user to MongoDB
    
    # Let's delete users for fun (in real-world, you'd do this with proper IDs)
    mysql_db.delete_user(user_id=1)  # Deleting user from MySQL
    mongo_db.delete_user(user_id=1)  # Deleting user from MongoDB, thanks!

# Please, please, please! Run the main function!
if __name__ == "__main__":
    main()
