# Radovan Novakovity
# Try it yourself 7-4.
#  Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value
#  As they enter each topping, print a message saying you’ll add that topping to their pizza

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