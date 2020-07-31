# Radovan Novakovity
# Try it yourself 9-8.
#  Write a separate Privileges class
#  The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7
#  Move the show_privileges() method to this class
#  Make a Privileges instance as an attribute in the Admin class
#  Create a new instance of Admin and use your method to show its privileges

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
        # Initialize an emtpy set of privileges
        self.privileges = Privileges()

# Creating a privileges attribute class
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

# Creating an instance from the admin class
administrator = Admin('zack', 'brown', 'zaown', 51)

# Making a list of privileges then storing it in a variable
administrator_privileges = [
    'can ban user',
    'can add post',
    'can delete post',
    ]
# Passing the stored list to the instance from the admin class
administrator.privileges.privileges = administrator_privileges

# Calling the method to show whats in the attributes list
administrator.privileges.show_privileges()