def  cityCountry(city, country):
    """Return a neatly formatted city and country."""
    place = f"{city}, {country}"
    return place.title()

location = cityCountry('minneapolis', 'united states')
print(location)

location = cityCountry('paris', 'france')
print(location)

location = cityCountry('toronto', 'canada')
print(location)