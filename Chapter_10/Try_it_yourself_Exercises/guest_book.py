# Radovan Novakovity
# Try it yourself 10-4.
#  Write a while loop that prompts users for their name
#  When they enter their name, print a greeting to the screen and add a line recording their visit in a file called guest_book.txt
#  Make sure each entry appears on a new line in the file

# Making a flag for the while loop
name_input = True

filename = 'guest_book.txt'

# Runs until the flag changes to false
while name_input:
    name = input("Hello, please state you name, otherwise if you wish to stop please write 'quit' ")

    if name == 'quit':
        # If user enters quit then the flag will be set to False, thus ending the while loop
        name_input = False
    else:
        # Opening the txt file and appending each guest to it
        with open(filename, 'a') as file_object:
            file_object.write(f"{name}\n")
            print(f"Hello, {name}, you have been added to the guest book.")