# Write a function that accepts two parameters: a city and country name
# The function should return a single string of the form city, country,
# such as satiago, chile. Store the function in a module called
# city_functions.py

# Modify the function so it requires a third parameter, population.


def get_formatted_name(city, country, population=''):
    """Generate a neatly formatted city, country - population xxx."""
    if population:
        full_name = f"{city.title()}, {country.title()} - population {population}"
    else:
        full_name = f"{city.title()}, {country.title()}"
    return full_name

