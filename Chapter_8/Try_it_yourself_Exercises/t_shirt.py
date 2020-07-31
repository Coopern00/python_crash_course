# Radovan Novakovity
# Try it yourself 8-3.
#  Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt
#  The function should print a sentence summarizing the size of the shirt and the message printed on it
#  Call the function once using positional arguments to make a shirt
#  Call the function a second time using keyword arguments

# Making a function to print the size of the shirt, and the text on it
def make_shirt(size, text):
    """Shows the size of the t-shirt, and the desired message on it"""
    print(f"\nThe size of the shirt is {size}, and the printed message on it is, {text}.")

# Calling the the t-shirt making function using positional arguments
make_shirt(42, 'Hello World')

# Calling the the t-shirt making function using keyword arguments
make_shirt(size=42, text='Hello World')