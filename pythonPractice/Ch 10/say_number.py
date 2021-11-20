import json

filename = 'fav_num.json'

with open(filename) as f:
    number = json.load(f)
    print(f"I know your favorite number! It's {number}")