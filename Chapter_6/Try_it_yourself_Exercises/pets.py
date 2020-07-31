# Radovan Novakovity
# Try it yourself 6-8.
#  Make several dictionaries, where each dictionary represents a different pet
#  In each dictionary, include the kind of animal and the owner’s name
#  Store these dictionaries in a list called pets
#  Next, loop through your list and as you do, print everything you know about each pet

coco = {
    'animal_kind': 'monkey',
    'owner_name': 'alex',
    }

molly = {
    'animal_kind': 'dog',
    'owner_name': 'jack',
    }

ollie = {
    'animal_kind': 'cat',
    'owner_name': 'jane',
    }

toby = {
    'animal_kind': 'parrot',
    'owner_name': 'bob',
    }

# Storing each dictionary in a list
pets = [coco, molly, ollie, toby]

# Loop through the list and print everything
print("\nAll the information about this list of pets: ")
for pet in pets:
    print(f"\tThe kind of animal: {pet['animal_kind'].title()}")
    print(f"\tThe owner's name: {pet['owner_name'].title()}\n")