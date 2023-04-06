import unittest
from exercise9 import *


class RollTheDiceTest(unittest.TestCase):
    def test_roll_dice_sum(self):

        expected_result = (167, 48)
        result = sum_roll_dice()

        self.assertEqual(expected_result, result)


unittest.main()
