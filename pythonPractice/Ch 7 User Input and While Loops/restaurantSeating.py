tableNumber = input("How many people are in your dinner group? ")
tableNumber = int(tableNumber)

if tableNumber >= 9:
    print("\nYou will have to wait for a table.")
else:
    print("\nYour table is ready.")