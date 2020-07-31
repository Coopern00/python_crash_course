# Radovan Novakovity
# Try it yourself 10-11.
#  Read program

import json

# Telling the user their favorite_number
filename = 'favorite_number.json'
with open(filename) as f:
    return_number = json.load(f)

print(f"I know your favorite number! It's {return_number}!")