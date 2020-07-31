# Radovan Novakovity
# Try it yourself 9-5.
#  Add an attribute called login_attempts to your User class from Exercise 9-3
#  Write a method called increment_login _attempts() that increments the value of login_attempts by 1
#  Write another method called reset_login_attempts() that resets the value of login_attempts to 0
#  Make an instance of the User class and call increment_login_attempts() several times
#  Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts()
#  Print login_attempts again to make sure it was reset to 0

# Making the User class
class User():
    """Making a user class."""
    
    def __init__(self, first_name, last_name, username, age):
        """Initializing the attributes."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """This prints a summary of the user's information."""
        print(f"The name of the user is: {self.first_name} {self.last_name}")
        print(f"The age of the user is: {self.age}")
        print(f"The username of the user is: {self.username}")

    def greet_user(self):
        """Print a personalied greeting to the user."""
        print(f"Welcome {self.username}, and have a nice day.\n")

    # A method that increments the value of user login attempts by 1
    def increment_login_attempts(self):
        """Increments the value of user login attempts by 1."""
        self.login_attempts += 1

    # A method that resets the value of user login attempts
    def reset_login_attempts(self):
        """This method resets the value of login_attempts to 0."""
        self.login_attempts = 0

# Making an instance from the class
user_one = User('tyler', 'woods', 'tywoo', 34)

# Calling the increment number a few times
user_one.increment_login_attempts()
user_one.increment_login_attempts()
user_one.increment_login_attempts()
user_one.increment_login_attempts()
print(f"\nThe number of login attempts from user: {user_one.login_attempts}")

# Calling the reset method
user_one.reset_login_attempts()
print(f"\nThe number of login attempts from user: {user_one.login_attempts}")