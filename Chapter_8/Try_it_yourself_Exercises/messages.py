# Radovan Novakovity
# Try it yourself 8-9.
#  Make a list containing a series of short text messages
#  Pass the list to a function called show_messages(), which prints each text message

# Making a function that is able to print a list if its passed to it
def show_messages(messages):
    """This function prints the messages from a list"""
    for message in messages:
        print(message)

messages = ['hello there', 'today is friday', 'it is sunny today',]
show_messages(messages)