with open('pi_digits.txt') as file_object:
    contents = file_object.read()


print(f"({contents})")
print(f"({contents.rstrip()})")