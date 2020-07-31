# Radovan Novakovity
# Try it yourself 9-1.
#  Make a class called Restaurant
#  The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type
#  Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open
#  Make an instance called restaurant from your class
#  Print the two attributes individually, and then call both methods

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
        print(f"The cousine in the restaurant is {self.cuisine_type}.")

    # Making the restaurant is open method
    def open_restaurant(self):
        """Prints that the restaurant is open."""
        print("\nThe restaurant is now open.")

# Making an instance from the Restaurant class
restaurant = Restaurant('salty sea', 'sea food')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Calling the methods
restaurant.describe_restaurant()
restaurant.open_restaurant()