import unittest
from src.quote import quote


class QuotePrecision(unittest.TestCase):
    def test_large(self):
        result = quote(10**20, 3)
        self.assertEqual(result, 10**20 * 3 * 900)
        self.assertIsInstance(result, int)
