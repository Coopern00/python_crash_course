# Radovan Novakovity
# Try it yourself 9-7.
#  An administrator is a special kind of user
#  Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 or Exercise 9-5
#  Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on
#  Write a method called show_privileges() that lists the administrator’s set of privileges
#  Create an instance of Admin, and call your method

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
        print(f"Welcome {self.username}, and have a nice day.")

# Creating an Admin child class from the User class
class Admin(User):
    """Represents a special user called admin."""

    def __init__(self, first_name, last_name, username, age):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, age)
        # Adding an attribute to the child class
        self.privileges = []

    # Creating a method to show whats in the attributes list
    def show_privileges(self):
        """Printing the contents of the privilages list."""
        print("Privileges: ")
        for privilege in self.privileges:
            print(f"\t{privilege}")

# Creating an instance from the admin class
administrator = Admin('zack', 'brown', 'zaown', 51)
administrator.privileges = [
    'can ban user',
    'can add post',
    'can delete post',
    ]

# Calling the method to show whats in the attributes list
administrator.show_privileges()