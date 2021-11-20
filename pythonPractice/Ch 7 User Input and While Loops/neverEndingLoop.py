prompt = "Please enter your age:"
prompt += "\n(Enter 'done' when you are finished.) "

while True:
    age = input(prompt)

    age = int(age)
    if age < 3:
        print("Your movie ticket is free.")
    elif age <= 12:
        print("Your movie ticket is $10.")
    elif age >= 13:
        print("Your movie ticket is $15.")