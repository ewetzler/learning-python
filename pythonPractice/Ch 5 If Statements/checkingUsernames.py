currentUsers = ['ewetzler', 'loomisdf', 'Chubbybunny1', 'Jane123', 'bouncygirl33']
newUsers = ['John', 'jane123', 'chubbybunny1', 'Mark', 'Mary']

for newUser in newUsers:
    # lowerCaseUsers = [user.lower() for user in currentUsers]
    lowerCaseUsers = []
    for user in currentUsers:
        lowerCaseUsers.append(user.lower())
    if newUser.lower() in lowerCaseUsers:
        print(f"The username {newUser} is not available.")
    else:
        print(f"The username {newUser} is available.")