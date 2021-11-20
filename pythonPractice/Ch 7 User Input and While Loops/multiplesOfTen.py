# Ask the user for a number
# Report whether the number is a multiple of 10 or not
number = input("Enter a number: ")
number = int(number)

if number % 10 == 0:
    print(f"\nThe number {number} is a multiple of 10.")
else:
    print(f"\nThe number {number} is not a multiple of 10.")