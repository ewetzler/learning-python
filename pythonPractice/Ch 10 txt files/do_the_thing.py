with open("guests.txt", 'r') as guests:
    output = ""
    count = 0
    while True:
        currLine = guests.readline().strip()
        output += currLine + "|"
        count += 1
        if count == 4:
            print(output)
            output = ""
            count = 0
