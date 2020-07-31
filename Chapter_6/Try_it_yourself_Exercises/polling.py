# Radovan Novakovity
# Try it yourself 6-6.
#  Use the code in favorite_languages.py
#  Make a list of people who should take the favorite languages poll
#  Include some names that are already in the dictionary and some that are not
#  Loop through the list of people who should take the poll
#  If they have already taken the poll, print a message thanking them for responding
#  If they have not yet taken the poll, print a message inviting them to take the poll

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

# Make a list of people who should take the poll
programmers = ['alex', 'jen', 'brandon', 'colton', 'phil', 'jack']

# Loop through the list
for person in programmers:
    if person in favorite_languages.keys():
        print(f"Hey {person.title()}, thanks for responding!\n")
    else:
        print(f"Hello there {person.title()}, I would like to invite you take participate in a poll!\n")