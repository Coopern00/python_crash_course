# Radovan Novakovity
# Try it yourself 9-10.
#  Using your latest Restaurant class, store it in a module
#  Make a separate file that imports Restaurant
#  Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly

# Importing the Restaurant module, so the class can be used
from restaurant_module import Restaurant

# Making an instance from the restaurant class
my_restaurant = Restaurant('mini italy', 'italian food')

# Calling a method from the restaurant class
my_restaurant.describe_restaurant()