class User:
    """Something"""

    def __init__(self, first_name, last_name, age, birth_date):
        """Initialize first and last name attributes."""
        self.first = first_name
        self.last = last_name
        self.age = age
        self.birth_date = birth_date

    def describe_user(self):
        """Print a summary of the user's info"""
        print(f"\nUser: \n\t{self.first}\n\t{self.last}\n\t{self.age}\n\t{self.birth_date}")

    def greet_user(self):
        """Print a personalized greeting to the user"""
        print(f"\nHello {self.first} {self.last}")

# user0 = User('Elana', 'Wetzler', '25', '7/31/1995')
# user1 = User('Daltin', 'Loomis', '25', '3/24/1995')
# user2 = User('Robert', 'Wetzler', '20', '4/16/2000')
#
# user0.describe_user()
# user0.greet_user()
# user1.describe_user()
# user1.greet_user()
# user2.describe_user()
# user2.greet_user()