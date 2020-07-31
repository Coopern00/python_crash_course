# Radovan Novakovity
# Try it yourself 10-3.
#  Write a program that prompts the user for their name
#  When they respond, write their name to a file called guest.txt

user_name = input("Hello, please write your name here: ")

filename = 'guest.txt'

with open(filename, 'w') as file_object:
    file_object.write(user_name)