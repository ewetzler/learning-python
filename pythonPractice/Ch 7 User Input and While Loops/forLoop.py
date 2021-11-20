pets = ['cat', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
for i in range(len(pets)):
    if pets[i] == 'cat':
        pets.pop(i)
print(pets)
