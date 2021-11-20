# Write a class called Employee.
# The __init__() method should take in a first name, last name,
# and annual salary, and store each of these as attributes.
# Write a method called give_raise() that adds $5,000 to the
# annual salary by default but also accepts a different raise amount.

class Employee:
    """Collect info for an employee."""

    def __init__(self, first_name, last_name, annual_salary):
        """Initialize the employee identification attributes."""
        self.first = first_name
        self.last = last_name
        self.salary = annual_salary

    def give_raise(self, salary_increase=5000):
        """Add $5,000 to the annual salary and accept a different amount."""
        self.salary += salary_increase

my_employee = Employee('Elana', 'Wetzler', 10000)

# print(my_employee.salary)
# my_employee.give_raise()
# print(my_employee.salary)