favoritePlaces = {
    'elana': ['minneapolis', 'hawaii'],
    'ella': ['bean bag', 'outside'],
    'carolyn': ['paris', 'norway'],
}

for name, places in favoritePlaces.items():
    print(f"\n{name.title()}:")
    for place in places:
        print(f"\t{place.title()}")