# Creating a module for Exercise 9-11.

"""Represent a simple user profile."""

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

class Admin(User):
    """Represents a special user called admin."""

    def __init__(self, first_name, last_name, username, age):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, age)
        self.privileges = Privileges()

class Privileges():
    """Represents admin privileges."""

    def __init__(self, privileges=[]):
        """Initialize the privileges."""
        self.privileges = privileges

    def show_privileges(self):
        """Printing the contents of the privileges list."""
        print("Privileges: ")
        for privilege in self.privileges:
            print(f"\t{privilege}")