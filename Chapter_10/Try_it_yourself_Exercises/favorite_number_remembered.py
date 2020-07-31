# Radovan Novakovity
# Try it yourself 10-12.
#  Combine the two programs from Exercise 10-11 into one file
#  If the number is already stored, report the favorite number to the user
#  If not, prompt for the user’s favorite number and store it in a file
#  Run the program twice to see that it works

import json

filename ='favorite_number_remembered.json'

try:
    with open(filename) as f:
        return_number = json.load(f)
except FileNotFoundError:
    favorite_number = input("Hello please tell us your favorite number: ")
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
        print("Your favorite number is stored.")
else:
    print(f"I know your favorite number! It's {return_number}!")