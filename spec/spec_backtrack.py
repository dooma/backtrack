__author__ = 'Călin Sălăgean'

import unittest
from lib.backtrack import Backtrack


class TestBacktrack(unittest.TestCase):
    def test_initialization(self):
        backtrack = Backtrack([1, 2, 3, 4, 5])
        self.assertIsInstance(backtrack, Backtrack)

    def test_validation(self):
        with self.assertRaisesRegex(AttributeError, "'input' attribute should be a list"):
            backtrack = Backtrack('1,2,3,4,5')

        with self.assertRaisesRegex(AttributeError, "'input' attribute should be a list"):
            backtrack = Backtrack([])

        with self.assertRaisesRegex(ValueError, "The element on position 0 should be integer or float number"):
            backtrack = Backtrack(['1asdf', 2, 3, 4, 5])

    def test_properties(self):
        backtrack = Backtrack([1, 2, 3, 4, 5])

        self.assertEqual(backtrack.array, [1, 2, 3, 4, 5])
        self.assertEqual(backtrack.result, [])

    def test_algorithm_valley(self):
        backtrack = Backtrack([1, 1, 2, 3, 4, 5])

        backtrack._Backtrack__permutation = [3, 1, 1, 2, 4, 5]
        self.assertTrue(backtrack.valley())

        backtrack._Backtrack__permutation = [3, 1, 2, 1, 4, 5]
        self.assertFalse(backtrack.valley())

    def test_issorted(self):
        self.assertTrue(Backtrack.issorted([1, 2, 3, 4]))
        self.assertTrue(Backtrack.issorted([3, 2, 1], reverse=True))

        self.assertFalse(Backtrack.issorted([1, 2, 4, 3]))
        self.assertFalse(Backtrack.issorted([3, 1, 2], reverse=True))

    def test_minimum_array(self):
        backtrack = Backtrack([1, 1, 2, 3, 4, 5])

        self.assertEqual(backtrack.minimum_array(2), [1, 1])

    def test_determine(self):
        backtrack = Backtrack([1, 1, 2, 3, 4, 5])

        backtrack.determine()