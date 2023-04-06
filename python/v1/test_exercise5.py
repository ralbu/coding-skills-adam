import unittest
from exercise5 import *


class HighestDivisionOfThree(unittest.TestCase):
    """Tests for function"""

    def test_highest_division_of_three_when_less_than_three(self):
        """When number is less than 3 it should return 0"""
        no_to_test = 2
        result = highest_divisor_of_three(no_to_test)

        self.assertEqual(0, result)

    def test_highest_division_of_three_when_three(self):
        """When number is 3 it should return 3"""
        no_to_test = 3
        result = highest_divisor_of_three(no_to_test)

        self.assertEqual(3, result)

    def test_highest_division_of_three_when_greater_than_three(self):
        """When number is greater than 3 it should calculate the correct number """
        no_to_test = 10
        result = highest_divisor_of_three(no_to_test)

        self.assertEqual(9, result)


unittest.main()
