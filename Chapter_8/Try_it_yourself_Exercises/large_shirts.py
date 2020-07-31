# Radovan Novakovity
# Try it yourself 8-4.
#  Modify the make_shirt() function so that shirts are large by default with a message that reads "I love Python"
#  Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message

# Making a function to print the size of the shirt, and the text on it
def make_shirt(size='large', text='I love Python'):
    """Shows the size of the t-shirt, and the desired message on it"""
    print(f"\nThe size of the shirt is {size.title()}, and the printed message on it is, {text.title()}.")

# Making a large shirt with the default arguments
make_shirt()

# Making a medium shirt with the default text argument
make_shirt('medium')

# Making a shirt with non-default arguments
make_shirt('small', 'tomorrow is wednesday')