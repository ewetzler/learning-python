class Restaurant:
    """A simple attempt to model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and  type attributes."""
        self.name = restaurant_name
        self.food = cuisine_type

    def describe_restaurant(self):
        """Simulate the restaurant name and what it serves."""
        print(f"The restaurant {self.name} "
              f"serves {self.food} food.")

    def open_restaurant(self):
        """Simulate the restaurant opening."""
        print(f"{self.name} is now open.")


restaurant = Restaurant('Chipotle', 'Mexican')
restaurant1 = Restaurant('McDonalds', 'Fast')
restaurant2 = Restaurant('Olive Garden', 'Italian')

# print(restaurant.name)
# print(restaurant.food)
restaurant.describe_restaurant()
# restaurant.open_restaurant()
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()

class IceCreamStand(Restaurant):
    """Represent aspects of a restaurant, specific to ice cream stands."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of the parent class."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Chocolate", "Vanilla", "Strawberry"]

    def print_flavors(self):
        """Display ice cream flavors."""
        # flavor_string = str(self.flavors).replace("[", "").replace("]", "")
        flavor_string = ", ".join(self.flavors)
        print(f"Today's ice cream flavors are {flavor_string}")

ice_cream_shop = IceCreamStand("Ella's Ice Cream", "Ice Cream")
ice_cream_shop.describe_restaurant()
ice_cream_shop.print_flavors()