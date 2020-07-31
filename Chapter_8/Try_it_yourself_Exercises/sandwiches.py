# Radovan Novakovity
# Try it yourself 8-12.
#  Write a function that accepts a list of items a person wants on a sandwich
#  The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered
#  Call the function three times, using a different number of arguments each time

def sandwich_order(*sandwich_ingredients):
    """Prints the summary of the ordered sandwich"""
    print("\nThe ordered sandwich is beign made from:")
    for sandwich_ingredient in sandwich_ingredients:
        print(f"- {sandwich_ingredient}")

sandwich_order('salami', 'cheese')
sandwich_order('fish', 'meat', 'salad')
sandwich_order('ham',)