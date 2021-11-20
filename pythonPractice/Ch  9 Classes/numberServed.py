class Restaurant:
    """A simple attempt to model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and  type attributes."""
        self.name = restaurant_name
        self.food = cuisine_type
        self.number_served = 2

    def describe_restaurant(self):
        """Simulate the restaurant name and what it serves."""
        print(f"The restaurant {self.name} "
              f"serves {self.food} food.")

    def open_restaurant(self):
        """Simulate the restaurant opening."""
        print(f"{self.name} is now open.")

    def set_number_served(self, total_customers):
        """Set the number of customers that have been served."""
        self.number_served = total_customers

    def increment_number_served(self, customers):
        """Increment the number of customers who've been served."""
        self.number_served += customers

restaurant = Restaurant('Chipotle', 'Mexican')

# print(restaurant.name)
# print(restaurant.food)
print(restaurant.number_served)
restaurant.set_number_served(22)
print(restaurant.number_served)
restaurant.increment_number_served(50)
print(restaurant.number_served)
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
