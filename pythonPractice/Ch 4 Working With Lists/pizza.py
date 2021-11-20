#Ex 4-1
#make a list of 3 pizzas
#use a for loop to print the name of each pizza
pizzas = ['veggie', 'pineapple', 'margarita', 'greek', 'buffalo']
#for pizza in pizzas:
#    print(f"I like {pizza} pizza.")
#print("I really love pizza!")

#print the message( The first three items in the list are:)
#then use a slice to print the first three items from the list
#print("The first three items in the list are:")
#for pizza in pizzas[:3]:
#    print(pizza)

# print message( Three items from the middle of the list are:)
# use slice to print three items from the middle of the list
#print("Three items from the middle of the list are:")
#for pizza in pizzas[1:4]:
#    print(pizza)

# print message(The last three items in the list are:)
#print("The last three items in the list are:")
#for pizza in pizzas[-3:]:
#    print(pizza)

#make a copy of the lists of pizzas and call it friend_pizzas
friend_pizzas = pizzas[:]

# add a new pizza to the original list
pizzas.append('mushroom')

# add a different pizza to friend_pizzas
friend_pizzas.append('supreme')

#prove you have two separate lists
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for friendPizza in friend_pizzas:
    print(friendPizza)

