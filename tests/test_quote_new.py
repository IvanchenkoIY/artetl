import unittest
from src.quote import quote

class QuoteNew(unittest.TestCase):
    def test_discount(self):
        self.assertEqual(quote(5, 2), 9000)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            quote(0, 1)
        with self.assertRaises(ValueError):
            quote(-1, 1)
        with self.assertRaises(ValueError):
            quote(1, 0)
        with self.assertRaises(ValueError):
            quote(True, 1)
        with self.assertRaises(ValueError):
            quote(1.5, 1)
