# Write a program that polls users about their dream vacation
responses = {}

pollingActive = True

while pollingActive:
    name = input("\nWhat is your name? ")
    response = input("If you could go anywhere, where would you go? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        pollingActive = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to travel to {response}.")

