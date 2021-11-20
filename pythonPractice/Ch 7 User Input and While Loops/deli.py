# Start with a list of sandwich orders
# and an empty list called finishedSandwiches
sandwichOrders = ['pastrami', 'ham and cheese', 'pastrami', 'turkey', 'pastrami', 'veggie']
finishedSandwiches = []

print("The deli has run out of pastrami.")

while 'pastrami' in sandwichOrders:
    sandwichOrders.remove('pastrami')

while sandwichOrders:
    currentSandwich = sandwichOrders.pop()

    print(f"I made your {currentSandwich} sandwich.")
    finishedSandwiches.append(currentSandwich)

# Display all finished sandwiches
print("\nThe following sandwiches have been made:")
for finishedSandwich in finishedSandwiches:
    print(finishedSandwich)
