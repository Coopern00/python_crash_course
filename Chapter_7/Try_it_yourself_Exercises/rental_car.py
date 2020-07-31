# Radovan Novakovity
# Try it yourself 7-1.
#  Write a program that asks the user what kind of rental car they would like
#  Print a message about that car, such as “Let me see if I can find you a Subaru.”

# Storing the question in a variable
prompt = "What kind of car would you like to rent? "

# Passing the prompt variable to the input() function
car = input(prompt)
print(f"\nLet me see if I can find you a {car}.")