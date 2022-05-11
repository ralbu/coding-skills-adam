import unittest
from exercise10 import *


class CalculateAvgPlayersTest(unittest.TestCase):
    def test_avg_players(self):
        players = [
            {'name': 'James', 'score': 200},
            {'name': 'Mary', 'score': 100},
            {'name': 'David', 'score': 30},
            {'name': 'John', 'score': 100},
            {'name': 'daniel', 'score': 70},
            {'name': 'Diana', 'score': 140},
        ]

        expected_result = {
            'J': 150,
            'M': 100,
            'D': 80
        }
        result = calculate_avg_players(players)

        self.assertEqual(expected_result, result)


unittest.main()
