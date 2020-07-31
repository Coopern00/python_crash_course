# Radovan Novakovity
# Try it yourself 9-6.
#  An ice cream stand is a specific kind of restaurant
#  Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 or Exercise 9-4
#  Either version of the class will work; just pick the one you like better
#  Add an attribute called flavors that stores a list of ice cream flavors
#  Write a method that displays these flavors
#  Create an instance of IceCreamStand, and call this method

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

# Making a child class of the Restaurant parent class
class IceCreamStand(Restaurant):
    """Represents a variant of restaurants."""

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initializes attributes from restaurant parent class.
        Then initialize attributes specific to an ice cream stand.
        """
        super().__init__(restaurant_name, cuisine_type)
        # Making the ice cream flavors list attribute for the child class
        self.flavors = []

    # Making a method that prints the ice cream flavors from the list
    def ice_cream_flavors(self):
        """Prints the ice cream flavors from the list."""
        print("Here is a the list of available flavors: ")
        for flavor in self.flavors:
            print(f"\t{flavor}")

# Making an instance from the icecreamstand
ice_cream_stand = IceCreamStand('refreshing cold', 'ice cream')
ice_cream_stand.flavors = ['banana', 'vanilla', 'strawberry']
 
ice_cream_stand.describe_restaurant()
# Calling the method for the flavors
ice_cream_stand.ice_cream_flavors()