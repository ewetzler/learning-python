# Add integers together and print a message if input is not
# an int

prompt = "\nGive me two numbers and I'll add them"

first_number = input(prompt + "\nFirst number: ")

second_number = input("\nSecond number: ")
try:
      answer = int(first_number) + int(second_number)
except ValueError:
    print("All inputs must be numbers.")
else:
    print(answer)