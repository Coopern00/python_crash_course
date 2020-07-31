# Radovan Novakovity
# Try it yourself 8-5.
#  Write a function called describe_city() that accepts the name of a city and its country
#  The function should print a simple sentence, such as Reykjavik is in Iceland
#  Give the parameter for the country a default value
#  Call your function for three different cities, at least one of which is not in the default country

def describe_city(city_name, country='US'):
    """Displays the name of the city and which country it is in"""
    print(f"\n{city_name} is in {country}.")

# Calling the funtion for two different cities
describe_city(city_name='Seattle')

describe_city('Atlanta')

# Calling the function with non default value
describe_city('Vancouver', 'Canada')