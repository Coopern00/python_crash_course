# Radovan Novakovity
# Try it yourself 9-12.
#  Store the User class in one module, and store the Privileges and Admin classes in a separate module
#  In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly

# Importing the classes from the modules
from admin_and_privileges_module import Admin

# Creating an instance from the admin class
administrator = Admin('joe', 'ball', 'joll', 44)

# Creating a list of privileges
administrator_privileges = [
    'can ban user',
    'can add post',
    'can delete post',
    ]

# Passing the stored list to the instance from the admin class
administrator.privileges.privileges = administrator_privileges

# Calling the method
administrator.privileges.show_privileges()