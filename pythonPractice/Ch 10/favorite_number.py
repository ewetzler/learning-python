# Write a program that prompts for the user's fav number
# Use json.dump to store this number in a file.
# Write a separate program that reads in this value and print the message
# "I know your fav number! It's ____"

import json

number = input("What is your favorite number? ")

filename = 'fav_num.json'
with open(filename, 'w') as f:
    json.dump(number, f)
