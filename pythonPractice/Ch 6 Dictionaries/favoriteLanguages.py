favoriteLanguages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

shouldPoll = ['clark', 'sarah', 'gwen', 'robert', 'jen']

for name in shouldPoll:
    if name in favoriteLanguages.keys():
        print(f"Thank you, {name.title()}, for taking the poll.")
    if name not in favoriteLanguages.keys():
        print(f"{name.title()}, please take the poll.")
