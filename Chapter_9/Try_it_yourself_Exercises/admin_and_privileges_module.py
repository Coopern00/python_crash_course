# Creating an Admin and Privileges class module for 9-12.

"""A set of classes that can be used to represent an admin user and its privileges."""

# Importing the User class module
from user_module import User

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