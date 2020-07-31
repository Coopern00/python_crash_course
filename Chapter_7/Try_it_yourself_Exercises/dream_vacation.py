# Radovan Novakovity
# Try it yourself 7-10.
#  Write a program that polls users about their dream vacation
#  Write a prompt similar to "If you could visit one place in the world, where would you go?"
#  Include a block of code that prints the results of the poll

# A dictionary to store user input
responses = {}

# Making a flag to later end the loop
poll_active = True

# Making a while loop to keep asking for user input until someone writes 'no'
while poll_active:
    # Storing the users name and vacation destination in different variables 
    name = input("\nWhat is your name? ")
    response = input("Which place would you like to visit as a dream vacation? ")
    # Placing the name as key inside the responses dictionary, and the vacation place as value
    responses[name] = response
    # This part is for asking the user for yes/no input, if the answer is no, then the flag is set to False for the loop to end
    repeat = input("Would you like to let another person respond? yes / no ")
    if repeat == 'no':
        poll_active = False
# Looping through the responses dictionary to show each persons response
print("Poll results: \n")
for name, response in responses.items():
    print(f"{name} would like to visit {response}.")