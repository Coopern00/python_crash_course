# Creating the Restaurant module for Exercise 9-10.

"""A class representing a restaurant."""

class Restaurant():
    """Creating a basis for restaurants."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the name and cousine type for the restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints the name and cousine type of the certain restaurant."""
        print(f"The name of the restaurant is {self.restaurant_name.title()}.")
        print(f"The cousine in the restaurant is {self.cuisine_type}.")

    def open_restaurant(self):
        """Prints that the restaurant is open."""
        print("\nThe restaurant is now open.")