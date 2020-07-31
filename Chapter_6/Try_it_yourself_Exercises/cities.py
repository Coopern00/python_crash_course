# Radovan Novakovity
# Try it yourself 6-11.
#  Make a dictionary called cities
#  Use the names of three cities as keys in your dictionary
#  Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city
#  The keys for each city’s dictionary should be something like country, population, and fact
#  Print the name of each city and all of the information you have stored about it

cities = {
    'los angeles': {
        'country': 'united states',
        'population': 4000000,
        'fact': 'It is the center of the nations film an television industry.',
        },
    
    'vancouver': {
        'country': 'canada',
        'population': 631490,
        'fact': 'It is among Canadas densest, most ethnically diverse cities.',
        },

    'hamburg': {
        'country': 'germany',
        'population': 1810000,
        'fact': 'Its crossed by hundreds of canals, and also contains large areas of parkland.',
        },
}

# Looping through the dictionaries nested inside a dictionary to extract information about each cities name and info
for name, information in cities.items():
    print(f"\nThe name of the city: {name.title()}")
    print(f"\tThe country which the city is part of: {information['country'].title()}")
    print(f"\tThe population of the city: {information['population']}")
    print(f"\tHere is a fact about the city: {information['fact']}")