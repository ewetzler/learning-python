# If a person is under  age 3 movie ticket is free
# between age 3 and 12 ticket is $10
# over age 12 ticket is $15
# white a loop where you ask users their age and tell them the cost of their
# movie ticket
prompt = "Please enter your age:"
prompt += "\n(Enter 'done' when you are finished.) "

while True:
    age = input(prompt)

    if age == 'done':
        break

    age = int(age)
    if age < 3:
        print("Your movie ticket is free.")
    elif age <= 12:
        print("Your movie ticket is $10.")
    elif age >= 13:
        print("Your movie ticket is $15.")
