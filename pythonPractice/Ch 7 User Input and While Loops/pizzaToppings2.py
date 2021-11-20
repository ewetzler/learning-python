# Use a conditional test in the while statement to stop the loop
prompt = "\nPlease enter a topping for your pizza:"
prompt += "\n(Enter 'complete' when you are finished.) "

topping = ""
while topping != 'complete':
    topping = input(prompt)

    if topping != 'complete':
        print(f"{topping.title()} will be added to your pizza.")
