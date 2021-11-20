class User:
    """Create a user"""

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

class Admin(User):
    """Admin privileges of a user"""

    def __init__(self, first_name, last_name, age, birth_date):
        """Initialize attributes of the parent class."""
        super().__init__(first_name, last_name, age, birth_date)
        self.privileges = ["Can add post", "Can delete post", "Can ban user"]

    def show_privileges(self):
        """List the admin's set of privileges."""
        for privilege in self.privileges:
            print(privilege)

admin = Admin('Sarah', 'Jamison', '15', '9/22/2005')
admin.describe_user()
admin.show_privileges()
