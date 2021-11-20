# Write a loop that prompts the user to enter a series of pizza toppings
# until  they enter a 'quit' value
# Print  a message saying you'll add the topping to their pizza for each topping
prompt = "\nPlease enter a topping for your pizza:"
prompt += "\n(Enter 'complete' when you are finished.) "

while True:
    topping = input(prompt)

    if topping == 'complete':
        break
    else:
        print(f"{topping.title()} will be added to your pizza.")
