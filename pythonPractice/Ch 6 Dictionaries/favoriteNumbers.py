favNumbers = {
    'daltin': ['42'],
    'elana': ['27', '7', '31'],
    'sarah': ['13', '29'],
    'clark': ['99'],
    'gwen': ['79', '62'],
}

for name, numbers in favNumbers.items():
    if len(numbers) == 1:
        print(f"{name.title()}'s favorite number is:")
        for number in numbers:
            print(f"\t{number}")
    else:
        print(f"{name.title()}'s favorite numbers are:")
        for number in numbers:
            print(f"\t{number}")


    # print(f"\n{name.title()}:")
    # for number in numbers:
    #     print(f"\t{number.title()}")