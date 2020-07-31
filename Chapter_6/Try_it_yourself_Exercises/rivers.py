# Radovan Novakovity
# Try it yourself 6-5.
#  Make a dictionary containing three major rivers and the country each river runs through
#  One key-value pair might be 'nile': 'egypt'
#  Use a loop to print a sentence about each river, such as "The Nile runs through Egypt"
#  Use a loop to print the name of each river included in the dictionary
#  Use a loop to print the name of each country included in the dictionary

major_rivers = {
    'danube': 'hungary',
    'thames': 'england',
    'seine': 'france',
    }

# Loop to print the sentence about each river
for river, country in major_rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\n")

# Loop to print the name of each river
for river in major_rivers.keys():
    print(river.title())

print("\n")

# Loop to print the name of each country
for country in major_rivers.values():
    print(country.title())