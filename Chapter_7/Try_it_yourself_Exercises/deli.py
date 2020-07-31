# Radovan Novakovity
# Try it yourself 7-8.
#  Make a list called sandwich_orders and fill it with the names of various sandwiches
#  Then make an empty list called finished_sandwiches
#  Loop through the list of sandwich orders and print a message for each order, such as "I made your tuna sandwich"
#  As each sandwich is made, move it to the list of finished sandwiches
#  After all the sandwiches have been made, print a message listing each sandwich that was made

sandwich_orders = [
    'Oven Roasted Chicken', 'Black Forest Ham', 
    'Spicy Italian', 'Steak & Cheese', 
    'Turkey Breast', 'Meatball Marinara',
    ]

finished_sandwiches = []

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