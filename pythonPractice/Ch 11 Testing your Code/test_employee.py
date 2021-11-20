# Write a test for Employee.
# Write two test methods, test_give_default_raise() and
# test_give_custom_raise().
# Use the setUp() method so you don't have to create a new employee
# instance in each test method. Run your test case, and make
# sure both tests pass.

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee"""

    def setUp(self):
        """Create a set of employee objects to use in all test methods"""
        self.my_employee = Employee('Elana', 'Wetzler', 10000)

    def test_give_default_raise(self):
        """Test that a default raise is added properly."""
        self.my_employee.give_raise()
        self.assertEqual(15000, self.my_employee.salary)


    def test_give_custom_raise(self):
        """Test that a custom raise is added properly."""
        self.my_employee.give_raise(3000)
        self.assertEqual(13000, self.my_employee.salary)

if __name__ == '__main__':
    unittest.main()