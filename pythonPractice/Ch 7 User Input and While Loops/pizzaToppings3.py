# Use an active variable to control how long the loop runs
prompt = "\nPlease enter a topping for your pizza:"
prompt += "\n(Enter 'complete' when you are finished.) "

active = True
while active:
    topping = input(prompt)

    if topping == 'complete':
        active = False
    else:
        print(f"{topping.title()} will be added to your pizza.")

