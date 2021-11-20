# Write a program that prompts the user for their name.
# When they respond, write their name to a file

filename = 'guest.txt'

message = input("What is your name? ")

with open(filename, 'w') as file_object:
    file_object.write(message)