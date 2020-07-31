# Radovan Novakovity
# Try it yourself 8-10.
#  Start with a copy of your program from Exercise 8-9
#  Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed
#  After calling the function, print both of your lists to make sure the messages were moved correctly

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
print("\nThis is for showing that the original list is now empty:")
for message in messages:
    print(f"\t{message}")

print("\nThis is for showing that the new list holds the text messages:")
for sent_message in sent_messages:
    print(f"\t{sent_message}")