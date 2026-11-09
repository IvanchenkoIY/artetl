import unittest
from src.quote import deposit


class Deposit(unittest.TestCase):
    def test_regular(self):
        self.assertEqual(deposit(1, 1), 300)
        self.assertEqual(deposit(5, 2), 2700)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            deposit(True, 1)
        with self.assertRaises(ValueError):
            deposit(1, True)
        with self.assertRaises(ValueError):
            deposit(0, 1)
        with self.assertRaises(ValueError):
            deposit(1, 0)
        with self.assertRaises(ValueError):
            deposit(-1, 1)
        with self.assertRaises(ValueError):
            deposit(1, -1)

    def test_large(self):
        result = deposit(10**20, 3)
        self.assertEqual(result, 10**20 * 810)
        self.assertIsInstance(result, int)
