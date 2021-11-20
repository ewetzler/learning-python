# Add integers together and print a message if input is not
# an int

prompt = "\nGive me two numbers and I'll add them"

while True:
    first_number = input(prompt + "\nFirst number: ")
    if first_number == "":
        break
    second_number = input("\nSecond number: ")
    if second_number == "":
        break
    try:
          answer = int(first_number) + int(second_number)
    except ValueError:
        print("All inputs must be numbers.")
    else:
        print(answer)