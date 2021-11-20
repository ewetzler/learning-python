filename = 'poll_results.txt'

prompt = "\nWhy do you like programming? "

while True:
    message = input(prompt)

    if message == "":
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(message + "\n")