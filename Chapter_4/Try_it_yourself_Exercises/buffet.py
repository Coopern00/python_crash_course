# Radovan Novakovity
# Try it yourself 4-13.
#  A buffet-style restaurant offers only five basic foods
#  Think of five simple foods, and store them in a tuple
#  Use a for loop to print each food the restaurant offers
#  Try to modify one of the items, and make sure that Python rejects the change
#  The restaurant changes its menu, replacing two of the items with different foods
#  Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu

basic_foods = ('pizza', 'hamburger', 'chicken wings', 'gyros', 'burrito')
for food in basic_foods:
	print(food)

# basic_foods[1] = 'egg'

print("\n")

basic_foods = ('fajita', 'taco', 'chicken wings', 'gyros', 'burrito')
for food in basic_foods:
	print(food)