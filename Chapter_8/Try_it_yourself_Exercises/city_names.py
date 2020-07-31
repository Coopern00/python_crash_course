# Radovan Novakovity
# Try it yourself 8-6.
#  Write a function called city_country() that takes in the name of a city and its country
#  The function should return a string formatted like this:
#  Call your function with at least three city-country pairs, and print the values that are returned

# Creating the function
def city_country(city, country):
    """This function returns the city and country"""
    return(f"{city.title()}, {country.title()}")

city = city_country('vancouver', 'canada')
print(city)

city = city_country('amsterdam', 'netherlands')
print(city)

city = city_country('seattle', 'united states')
print(city)