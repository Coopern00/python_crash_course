# Radovan Novakovity
# Try it yourself 4-11.
#  Start with your program from Exercise 4-1
#  Make a copy of the list of pizzas, and call it friend_pizzas
#  Then, do the following
#  Add a new pizza to the original list
#  Add a different pizza to the list friend_pizzas
#  Prove that you have two separate lists
#  Print the message "My favorite pizzas are:", and then use a for loop to print the first list
#  Print the message "My friend’s favorite pizzas are:", and then use a for loop to print the second list
#  Make sure each new pizza is stored in the appropriate list

#4-1. part
pizzas = ['pepperoni', 'cheese', 'mushroom']

for pizza in pizzas:
	print(pizza)

print("\n")

for pizza in pizzas:
	print(f"I like {pizza} pizza.\n")

print("I really love pizzas!")

#4-11. part

friend_pizzas = pizzas[:]

pizzas.append('texas')
friend_pizzas.append('dallas')

print("\nMy favorite pizzas are:")
for pizza in pizzas:
	print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)