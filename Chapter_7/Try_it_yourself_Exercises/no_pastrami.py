# Radovan Novakovity
# Try it yourself 7-9.
#  Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times
#  Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders
#  Make sure no pastrami sandwiches end up in finished_sandwiches

sandwich_orders = [
    'Oven Roasted Chicken', 'Pastrami', 'Black Forest Ham', 
    'Spicy Italian', 'Steak & Cheese', 'Pastrami',
    'Pastrami', 'Turkey Breast', 'Meatball Marinara',
    ]

finished_sandwiches = []

# printing a message that deli ran out of pastrami
print("We would like to inform customers that we are out of 'pastrami' sandwiches.\n")

# Loops until all instances of 'pastrami' has been removed from the orders list
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

# Loops until the sandwich_order list becomes emtpy
while sandwich_orders:
    # Removing a sandwich from the end of the list
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich} sandwich.")
    # After removing it from the original list, placing it in the destination list
    finished_sandwiches.append(current_sandwich) 

print("\nThe list of sandwiches which were made:")

# This for loop is for showing what sandwiches were made 
for sandwich in finished_sandwiches:
    print(f"\t{sandwich}")