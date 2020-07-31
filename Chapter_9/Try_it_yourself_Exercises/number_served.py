# Radovan Novakovity
# Try it yourself 9-4.
#  Start with your program from Exercise 9-1
#  Add an attribute called number_served with a default value of 0
#  Create an instance called restaurant from this class
#  Print the number of customers the restaurant has served, and then change this value and print it again
#  Add a method called set_number_served() that lets you set the number of customers that have been served
#  Call this method with a new number and print the value again
#  Add a method called increment_number_served() that lets you increment the number of customers who’ve been served
#  Call this method with any number you like that could represent how many customers were served in, say, a day of business

#Creating the restaurant class
class Restaurant():
    """Creating a basis for restaurants."""

    # Making the init method
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the name and cousine type for the restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    # Making the restaurant description method
    def describe_restaurant(self):
        """Prints the name and cousine type of the certain restaurant."""
        print(f"The name of the restaurant is {self.restaurant_name.title()}.")
        print(f"The cousine in the restaurant is {self.cuisine_type}.")

    # Making the restaurant is open method
    def open_restaurant(self):
        """Prints that the restaurant is open."""
        print("\nThe restaurant is now open.")

    # Adding a method that lets the number of customers served to be set
    def set_number_served(self, number_served):
        """Allows the number of customers to be set."""
        self.number_served = number_served

    # Adding a method that lets the number of customers to be incremented
    def increment_number_served(self, adding_customers):
        """Add the given amount to the customers number"""
        self.number_served += adding_customers

# Making an instance from the restaurant class
restaurant = Restaurant('salty sea', 'sea food')

# Printing the number of customers that restaurant has served
print(f"\nThe number of customers the restaurant has served: {restaurant.number_served}")
# Modifying the number_served attributes value and then print it
restaurant.number_served = 1
print(f"\nThe number of customers the restaurant has served: {restaurant.number_served}")

# Modifying the number_served with a method and then print it
restaurant.set_number_served(4)
print(f"\nThe number of customers the restaurant has served: {restaurant.number_served}")

# Incrementing an attribute's number through a method
restaurant.increment_number_served(6)
print(f"\nThe number of customers the restaurant has served: {restaurant.number_served}")