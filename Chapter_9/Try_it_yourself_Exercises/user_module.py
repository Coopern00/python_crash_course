# Creating the User class module for 9-12

"""A class that can be used to represent a user."""

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
        print("The name of the user is: " + self.first_name + " " + self.last_name +
            "\nThe age of the user is: " + str(self.age) +
            "\nThe username of the user is: " + self.username)

    def greet_user(self):
        """Print a personalied greeting to the user."""
        print("Welcome " + self.username + ", and have a nice day.\n")
