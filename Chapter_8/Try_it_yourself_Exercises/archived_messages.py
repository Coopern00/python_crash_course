# Radovan Novakovity
# Try it yourself 8-11.
#  Start with your work from Exercise 8-10
#  Call the function send_messages() with a copy of the list of messages
#  After calling the function, print both of your lists to show that the original list has retained its messages

# Making a function that is able to print a list if its passed to it
def show_messages(messages):
    """This function prints the messages from a list"""
    for message in messages:
        print(message)

# Making a function which iterates through a passed list and adds them to another list
def send_messages(messages):
    """Prints each text message before moving it to a new list"""
    while messages:
        for message in messages:
            print(message)
            message = messages.pop()
            sent_messages.append(message)

messages = ['hello there', 'today is friday', 'it is sunny today',]
# Build a new List to hold the sent messages
sent_messages = []

# Calling the function with a copy of the original list
send_messages(messages[:])

# Printing both lists
print("\nThis is for showing that the original list still has all the text messages:")
for message in messages:
    print(f"\t{message}")

print("\nThis is for showing that the new list holds the text messages from the copied list:")
for sent_message in sent_messages:
    print(f"\t{sent_message}")