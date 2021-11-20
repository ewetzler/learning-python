# Use a dictionary to store info about a person you know
# Store their first name, last name, age, and city they live in
people = {
    'daltin': {
        'firstName': 'daltin',
        'lastName': 'loomis',
        'age': 25,
        'city': 'minneapolis',
    },

    'sarah': {
        'firstName': 'sarah',
        'lastName': 'jamison',
        'age': 14,
        'city': 'pittsburgh',
    },

    'robert': {
        'firstName': 'robert',
        'lastName': 'wetzler',
        'age': 20,
        'city': 'columbus',
    },
}

for person, personInfo in people.items():
    print(f"\nPerson: {person}")
    fullName = f"{personInfo['firstName']} {personInfo['lastName']}"
    age = personInfo['age']
    location = personInfo['city']

    print(f"\tFull Name: {fullName.title()}")
    print(f"\tAge: {age}")
    print(f"\tLocation: {location.title()}")


