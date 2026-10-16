import unittest

from route_price import discounted_total


class DiscountTests(unittest.TestCase):
    def test_ten_percent(self):
        self.assertEqual(discounted_total([100, 200], 10), 270.0)

    def test_full_discount(self):
        self.assertEqual(discounted_total([100], 100), 0)


if __name__ == "__main__":
    unittest.main()
