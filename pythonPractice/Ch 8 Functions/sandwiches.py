# Function that accepts a list of items a person wants on a sandwich.
# The function should have 1 parameter that collects as many items as the function
# call provides, and it should print a summary of the sandwich being ordered.
# Call the function three times, using a different number of args each time.

def make_sandwich(*items):
    """Summarize the sandwich we are about to make."""
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")


make_sandwich('ham', 'cheese', 'mayo')
make_sandwich('salami', 'onion', 'mustard')
make_sandwich('turkey', 'mustard', 'lettuce')
