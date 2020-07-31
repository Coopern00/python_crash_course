# Radovan Novakovity
# Try it yourself 9-2.
#  Start with your class from Exercise 9-1
#  Create three different instances from the class, and call describe_restaurant() for each instance

#Creating the restaurant class
class Restaurant():
    """Creating a basis for restaurants."""

    # Making the init method
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the name and cousine type for the restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    # Making the restaurant description method
    def describe_restaurant(self):
        """Prints the name and cousine type of the certain restaurant."""
        print(f"The name of the restaurant is {self.restaurant_name.title()}.")
        print(f"The cousine in the restaurant is {self.cuisine_type}.\n")

    # Making the restaurant is open method
    def open_restaurant(self):
        """Prints that the restaurant is open."""
        print("\nThe restaurant is now open.")

# Part 9-2.
# Making three instances from the restaurant class
# Instance 1
first_restaurant = Restaurant('salty sea', 'sea food')
first_restaurant.describe_restaurant()

# Instance 2
second_restaurant = Restaurant('mongol food invasion', 'far east food')
second_restaurant.describe_restaurant()

# Instance 3
third_restaurant = Restaurant('chili america', 'mexican food')
third_restaurant.describe_restaurant()