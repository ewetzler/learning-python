cities = {
    'paris': {
       'country': 'france',
       'population': 2000000,
       'fact': 'French is the language spoken here.',
    },

    'minneapolis': {
        'country': 'united states',
        'population': 2000000,
        'fact': 'The vikings are the football team here.',
    },

    'cincinnati': {
        'country': 'united states',
        'population': 2000000,
        'fact': 'The bengals are the football team here.',
    }
}

for city, cityInfo in cities.items():
    print(f"\nCity: {city.title()}")
    country = cityInfo['country']
    population = cityInfo['population']
    fact = cityInfo['fact']

    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {population}")
    print(f"\tFact: {fact}")