# Radovan Novakovity
# Try it yourself 6-9.
#  Make a dictionary called favorite_places
#  Think of three names to use as keys in the dictionary, and store one to three favorite places for each person
#  To make this exercise a bit more interesting, ask some friends to name a few of their favorite places
#  Loop through the dictionary, and print each person’s name and their favorite places

favorite_places = {
    'alex': ['texas', 'ohio'],
    'jack': ['grand canyon'],
    'bob': ['montana', 'idaho', 'Arizona'],
    }

# Looping through the dictionary to display everyones name, and favorite place(s)
for name, places in favorite_places.items():
    if len(places) > 1:
        print(f"\n{name.title()}'s favorite places are: ")
    else:
        print(f"\n{name.title()}'s favorite place is: ")
    for place in places:
            print(f"\t{place.title()}")