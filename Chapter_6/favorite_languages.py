# Dictionary of similar objects
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

    #print("Sarah's favorite language is " +
    #    favorite_languages['sarah'].title() +
    #    ".")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# Looping through all the keys in a dictionary
for name in favorite_languages.keys():
    print(name.title())

    # Print message to certain people from the dictionary
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"{name.title()}, I see you love {language}!")

    # To find out if Erin took the poll
if 'erin' not in favorite_languages.keys():
    print("\nErin, please take our poll!")

# Looping through a dictionary's keys in order
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()} + ", thank you for taking the poll")

# Looping through all values in a dictionary
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# To see each language chosen without repetition, set()
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# Nesting a list inside a dictionary
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
       print(f"\t{language.title()}")