# Test the function in city_functions.py
# Import unittest and the function you are testing

import unittest
from city_functions import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Do names like 'Paris, France' work?"""
        formatted_name = get_formatted_name('paris', 'france')
        self.assertEqual(formatted_name, 'Paris, France')


    def test_city_country_population(self):
        """Do names like 'Paris, France - population xxx' work?"""
        formatted_name = get_formatted_name('paris', 'france', '2000000')
        self.assertEqual(formatted_name, 'Paris, France - population 2000000')


if __name__ == '__main__':
    unittest.main()
