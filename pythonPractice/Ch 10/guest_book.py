filename = 'guest_book.txt'

prompt = "\nWhat is your name?"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    message = input(prompt)

    if message == 'quit':
        break
    else:
        print(f"Hello {message.title()}!")
        with open(filename, 'a') as file_object:
            file_object.write(message + "\n")