import unittest
from src.route_price import discounted_total

class PriceBaseline(unittest.TestCase):
    def test_no_discount(self):
        self.assertEqual(discounted_total([100, 200], 0), 300)
    def test_empty(self):
        self.assertEqual(discounted_total([], 10), 0)
