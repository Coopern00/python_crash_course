# Radovan Novakovity
# Try it yourself 9-3.
#  Make a class called User
#  Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile
#  Make a method called describe_user() that prints a summary of the user's information
#  Make another method called greet_user() that prints a personalized greeting to the user
#  Create several instances representing different users, and call both methods for each user

# Making the User class
class User():
    """Making a user class."""
    
    def __init__(self, first_name, last_name, username, age):
        """Initializing the attributes."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.age = age

    def describe_user(self):
        """This prints a summary of the user's information."""
        print(f"The name of the user is: {self.first_name} {self.last_name}")
        print(f"The age of the user is: {self.age}")
        print(f"The username of the user is: {self.username}")
        
    def greet_user(self):
        """Print a personalied greeting to the user."""
        print(f"Welcome {self.username}, and have a nice day.\n")

# Creating several instances from the User class
# User 1
user_one = User('tyler', 'woods', 'tywoo', 34)
user_one.describe_user()
user_one.greet_user()

# User 2
user_two = User('juliana', 'black', 'juli', 42)
user_two.describe_user()
user_two.greet_user()

# User 3
user_three = User('henry', 'colber', 'hen', 29)
user_three.describe_user()
user_three.greet_user()