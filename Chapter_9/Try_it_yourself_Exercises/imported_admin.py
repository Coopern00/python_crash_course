# Radovan Novakovity
# Try it yourself 9-11.
#  Start with your work from Exercise 9-8
#  Store the classes User, Privileges, and Admin in one module
#  Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly

# Importing classes from the admin_module
from admin_module import User, Admin, Privileges

# Making an instance from the Admin class
administrator = Admin('john', 'green', 'grohn', 31)

# Creating a list of privileges
administrator_privileges = [
    'can ban user',
    'can add post',
    'can delete post',
    ]

# Passing the stored list to the instance
administrator.privileges.privileges = administrator_privileges

# Calling the method
administrator.privileges.show_privileges()