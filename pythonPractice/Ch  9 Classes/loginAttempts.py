class User:
    """Something"""

    def __init__(self, first_name, last_name, age, birth_date, login_attempts):
        """Initialize first and last name attributes."""
        self.first = first_name
        self.last = last_name
        self.age = age
        self.birth_date = birth_date
        self.login_attempts = login_attempts

    def describe_user(self):
        """Print a summary of the user's info"""
        print(f"\nUser: \n\t{self.first}\n\t{self.last}\n\t{self.age}\n\t{self.birth_date}")

    def greet_user(self):
        """Print a personalized greeting to the user"""
        print(f"\nHello {self.first} {self.last}")

    def increment_login_attempts(self):
        """Increment login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempts to 0."""
        self.login_attempts = 0

user0 = User('Elana', 'Wetzler', '25', '7/31/1995', 1)
user1 = User('Daltin', 'Loomis', '25', '3/24/1995', 4)
user2 = User('Robert', 'Wetzler', '20', '4/16/2000', 7)

user0.increment_login_attempts()
user0.increment_login_attempts()
user0.increment_login_attempts()
print(user0.login_attempts)
user0.reset_login_attempts()
print(user0.login_attempts)

