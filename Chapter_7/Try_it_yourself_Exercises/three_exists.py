# Radovan Novakovity
# Try it yourself 7-6.
#  Write different versions of either Exercise 7-4 or Exercise 7-5 that do each of the following at least once: 
#  Use a conditional test in the while statement to stop the loop
#  Use an active variable to control how long the loop runs
#  Use a break statement to exit the loop when the user enters a 'quit' value

# Version 1

prompt = "\nPlease enter the toppings you wish to have on your pizza!:"
# Building a multi-line string adding the option of quitting the pizza making process
prompt += "\nIf you think your pizza is done, simply type the word 'quit'! "

# This loop will display the pizza toppings
while True:
    pizza_topping = input(prompt)
    # If the user input is 'quit' then it breaks the loop and quit the program
    if pizza_topping == 'quit':
        print("\nYour pizza is finished!")
        break
    # Else it will just keep displaying the toppings 
    else:
        print(f"\nGreat! We'll add {pizza_topping} on your pizza.")

# Version 2

prompt = "\nPlease enter the toppings you wish to have on your pizza!:"
# Building a multi-line string adding the option of quitting the pizza making process
prompt += "\nIf you think your pizza is done, simply type the word 'quit'! "

# This is a flag variable for the while loop,
active = True

# This loop will display the pizza toppings
while active:
    pizza_topping = input(prompt)
    # If the user input is 'quit' then it breaks the loop and quit the program
    if pizza_topping == 'quit':
        print("\nYour pizza is finished!")
        # Changing the value of active to false so it will end the while loop 
        active = False
    # Else it will just keep displaying the toppings 
    else:
        print(f"\nGreat! We'll add {pizza_topping} on your pizza.")