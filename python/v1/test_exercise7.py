import unittest
from exercise7 import *


class SumOfAllNumbersTest(unittest.TestCase):

    def test_sum_all_numbers(self):
        result = sum_of_all_numbers_using_list(3)

        self.assertEqual(6, result)

    def test_sum_all_numbers_large(self):
        result = sum_of_all_numbers_using_list(91)

        self.assertEqual(4186, result)

    def test_sum_all_numbers_by_formula(self):
        result = sum_of_all_numbers_by_formula(3)

        self.assertEqual(6, result)


    def test_sum_all_numbers_by_formula_large(self):
        result = sum_of_all_numbers_by_formula(91)

        self.assertEqual(4186, result)


unittest.main()
