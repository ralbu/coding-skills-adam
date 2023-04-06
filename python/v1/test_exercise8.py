import unittest
from exercise8 import *

class GenerateNumbersTest(unittest.TestCase):
    def test_generate_odd_numbers(self):
        result = generate_odd_range(28)
        expected_result = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27]

        self.assertEqual(expected_result, result)

    def test_square_numbers(self):
        result = generate_square_numbers(1, 2)
        expected_result = [1, 4]

        self.assertEqual(expected_result, result)

    def test_square_numbers_larger(self):
        result = generate_square_numbers(1, 9)
        expected_result = [1, 4, 9, 16, 25, 36, 49, 64, 81]

        self.assertEqual(expected_result, result)

    def test_top_three(self):
        result = get_top_three()
        expected_result = [98, 81, 66]

        self.assertEqual(expected_result, result)


unittest.main()
