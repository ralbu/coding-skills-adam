import unittest
from exercise6 import *


class FruitsTest(unittest.TestCase):

    def test_list_all_the_fruit_in_the_basket(self):
        """List all the fruits in the basket """
        result = list_all_fruits_in_the_basket()

        self.assertEqual('Apple, Banana, Mango, Dragon fruit', result)

    def test_the_basket_contains_fruit(self):
        """The basket contains the fruit 'Banana'"""
        fruit_in_the_basket = 'Banana'
        result = does_the_basket_contain_fruit(fruit_in_the_basket)

        self.assertTrue(result)

    def test_the_basket_dos_Not_contain_fruit(self):
        """The basket does NOT contain the fruit 'Lychee'"""
        fruit_not_in_the_basket = 'Lychee'
        result = does_the_basket_contain_fruit(fruit_not_in_the_basket)

        self.assertFalse(result)

    def test_get_last_fruits(self):
        """Get the last fruit from the basket"""
        result = get_last_fruits()

        self.assertEqual(result, 'dragon fruit')

    def test_add_new_fruit_to_basket(self):
        """Add a new fruit to the basket"""
        new_fruit = 'Lychee'
        result = add_fruit(new_fruit)

        expected_basket= ['apple', 'banana', 'mango', 'dragon fruit', 'lychee']

        self.assertEqual(result, expected_basket)

    def test_add_fruit_in_the_middle(self):
        """Add a new fruit in the middle of the basket"""
        expected_basket = ['apple', 'banana', 'orange', 'mango', 'dragon fruit']

        result = add_fruit_in_the_middle('orange')

        self.assertEqual(result, expected_basket)

    def test_remove_banana_from_basket(self):
        """Remove banana from the basket"""

        expected_basket = ['apple', 'mango', 'dragon fruit']
        result = remove_banana_from_basket()

        self.assertEqual(result, expected_basket)

    def test_remove_last_two_fruits(self):
        """Remove last two fruits from the basket"""
        basket = ['apple', 'banana', 'mango', 'dragon fruit']
        result = remove_last_two_fruits_from_basket(basket)

        self.assertEqual(result, 'mango, dragon fruit')

    def test_remove_banana(self):
        """Remove banana from the basket"""

        expected_basket = ['apple', 'mango', 'dragon fruit']
        result = remove_fruit('banana')

        self.assertEqual(expected_basket, result)

    def test_remove_mango(self):
        """Remove mango from the basket"""

        expected_basket = ['apple', 'banana', 'dragon fruit']
        result = remove_fruit('mango')

        self.assertEqual(expected_basket, result)

unittest.main()
