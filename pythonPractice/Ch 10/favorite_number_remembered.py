# Combine favorite_number.py and say_number.py into one file.
# If the number is already stored, report the favorite number to the user.
# If not, prompt for the user's fav number and store it in a file.

import json

filename = 'fav_num.json'
try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("What is your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(number, f)
else:
    print(f"I know your favorite number! It's {number}")
