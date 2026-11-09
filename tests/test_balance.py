import unittest
from src.quote import quote, deposit, remaining_balance


class Balance(unittest.TestCase):
    def test_regular(self):
        self.assertEqual(remaining_balance(1, 1), 700)
        self.assertEqual(remaining_balance(5, 2), 6300)
        self.assertEqual(deposit(1, 1) + remaining_balance(1, 1), quote(1, 1))
        self.assertEqual(deposit(5, 2) + remaining_balance(5, 2), quote(5, 2))

    def test_invalid(self):
        with self.assertRaises(ValueError):
            remaining_balance(True, 1)
        with self.assertRaises(ValueError):
            remaining_balance(1, True)
        with self.assertRaises(ValueError):
            remaining_balance(0, 1)
        with self.assertRaises(ValueError):
            remaining_balance(1, 0)
        with self.assertRaises(ValueError):
            remaining_balance(-1, 1)
        with self.assertRaises(ValueError):
            remaining_balance(1, -1)

    def test_large(self):
        result = remaining_balance(10**20, 3)
        self.assertEqual(result, 10**20 * 1890)
        self.assertIsInstance(result, int)
