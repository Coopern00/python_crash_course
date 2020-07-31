"""Functions for working with cities."""

def city_country(city, country, population=0):
    """
    Returns City, Country,
    and optional population neatly formatted.
    """
    if population:
        formatted_city_country = (f"{city.title()}, {country.title()}" +
        f" population - {population}")
    else:
        formatted_city_country = f"{city.title()}, {country.title()}"
    return formatted_city_country