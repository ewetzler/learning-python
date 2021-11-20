#excercise 3-4
#make a list that includes at least three people to ivite to dinner
#use the list to print a message to each person, inviting them to dinner
guests = ['obama', 'daltin', 'lin']
guests[0] = 'RBG'
print(f"Hello {guests[0].title()}, {guests[1].title()}, and {guests[2].title()}.  I have found a bigger dinner table and will be able to invite 3 more guests.")
#use insert() to add one guest to the begining of the list
#use insert() to add one guest to the middle of the list
#use append() to add a guest to the end of the list
guests.insert(0, 'doctor')
guests.insert(2, 'loreli')
guests.append('luke')
msg0 = f"Dear {guests[0].title()}, please join me for dinner."
msg1 = f"Dear {guests[1].title()}, please join me for dinner."
msg2 = f"Dear {guests[2].title()}, please join me for dinner."
msg3 = f"Dear {guests[3].title()}, please join me for dinner."
msg4 = f"Dear {guests[4].title()}, please join me for dinner."
msg5 = f"Dear {guests[5].title()}, please join me for dinner."
invites = f"{msg0}\n{msg1}\n{msg2}\n{msg3}\n{msg4}\n{msg5}"
print(invites)
#add a new line that prints a message saying you can only invite two people
print("Hello all, unfortunatly the dinner table won't arrive in time for dinner and I can only invite two guests.")
#use pop()to remove guests from the list one at a time until only two names remain
#each time you pop a name from the list print a message to that person letting them know you're sorry
uninvite0 = guests.pop(0)
print(f"Dear {uninvite0.title()}, unfortualtly you will not be able to attend the dinner.")
uninvite1 = guests.pop(0)
print(f"Dear {uninvite1.title()}, unfortualtly you will not be able to attend the dinner.")
uninvite2 = guests.pop(1)
print(f"Dear {uninvite2.title()}, unfortualtly you will not be able to attend the dinner.")
uninvite3 = guests.pop(2)
print(f"Dear {uninvite3.title()}, unfortualtly you will not be able to attend the dinner.")
print(guests)
print(f"Dear {guests[0].title()}, you may still attend the dinner.")
print(f"Dear {guests[1].title()}, you may still attend the dinner.")
#del  guests[0]
#del guests[0]
#print(guests)

