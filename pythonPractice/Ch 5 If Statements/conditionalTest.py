# Ex 5-1
# Write a series of conditional tests
# Print a statement describing each test and your prediction
# for the results of each test
# create 10 tests
# have 5 tests evaluate to True and 5 evaluate to False

# Test 1
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

# Test 2
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# Test 3
dog = 'lab'
print("\nIs dog == 'lab'? I predict True.")
print(dog == 'lab')

# Test 4
print("\nIs dog == 'poodle'? I predict False.")
print(dog == 'poodle')

# Test 5
breeds  = ['lab', 'pug', 'poodle', 'hound']
print("\nIs 'lab' in breeds? I predict True.")
print('lab' in breeds)

# Test 6
print("\nIs 'poodle' in breeds? I predicts True")
print('poodle' in breeds)

# Test 7
print("\nIs 'corgi' in breeds? I predict False.")
print('corgi' in breeds)

# Test 8
print("\nIs 'beagle' in breeds? I predict False.")
print('beagle' in breeds)

# Test 9
print("\nIs dog  in breeds? I predict True.")
print(dog in breeds)

# Test 10
print("\nIs car in breeds? I predict False.")
print(car in  breeds)

# Test for equality and inequality with strings
car = 'subaru'
print("\nIs car == 'subaru'? I predict True.")
print(car == 'subaru')

if car != 'honda':
    print(f"\nThis is not a honda. This is a {car}.")

# Test using the lower() metohd
friend = "Daltin"
print("\nIs friend == daltin? I predict true.")
print(friend.lower() == 'daltin')

# Numerical test involving equality and inequality, greater than and less than
# greater than or equal to, and less than or equal to
age = 18
print("\nIs age == 18? I predict true.")
print(age == 18)

print("\nIs age == 19? I predicts false.")
print(age ==19)

if age != 20:
    print(f"\n{age} is not the correct age.")

print("\nIs age < 20? I predict true.")
print(age < 20)

print("\nIs age > 20? I predict false.")
print(age > 20)

print("\nIs age >= 4? I predict true.")
print(age >= 4)

print("\nIs age <= 6? I predict false.")
print(age <= 6)

# Test using the and and or keywords
age_0 = 23
age_1 = 19
print("\nAre age 0 and 1 both >= 20? I predict false.")
print(age_0 >= 20  and age_1 >= 20)

print("\nIs one age 0 and 1 >= 20? I predict true.")
print(age_0 >= 20 or age_1 >= 20)

# Test whether an item is not in a list
breeds  = ['lab', 'pug', 'poodle', 'hound']
print("\nIs  doodle  not in breeds? I predict true.")
print('doodle' not in breeds)