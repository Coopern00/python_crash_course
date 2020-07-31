# Radovan Novakovity
# Try it yourself 6-7.
#  Start with the program you wrote for Exercise 6-1
#  Make two new dictionaries representing different people, and store all three dictionaries in a list called people
#  Loop through your list of people
#  As you loop through the list, print everything you know about each person

person_1 = {
    'first_name': 'Alex',
    'last_name': 'Black',
    'age': 38,
    'city': 'Atlanta',
    }

person_2 = {
    'first_name': 'Jacob',
    'last_name': 'Green',
    'age': 26,
    'city': 'Baltimore',
    }

person_3 = {
    'first_name': 'Jim',
    'last_name': 'Brown',
    'age': 41,
    'city': 'Seattle',
    }

# Putting the dictionaries inside a list
people = [person_1, person_2, person_3]

# Output all the information from the people's dictionary in the list
for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print("\nAll the information about the person: ")
    print(f"\tFull name: {full_name.title()}")
    print(f"\tAge: {person['age']}")
    print(f"\tCity: {person['city']}")