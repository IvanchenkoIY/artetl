import unittest

from src.route_price import booking_quote


class QuoteTests(unittest.TestCase):
    def test_amount(self):
        q = booking_quote(1000, 2, 1, 10, 30)
        self.assertEqual(q["total"], 1800)
        self.assertEqual(q["deposit"], 540)
        self.assertEqual(q["balance"], 1260)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            booking_quote(-1, 2, 1, 10, 30)
        with self.assertRaises(ValueError):
            booking_quote(1000, 0, 1, 10, 30)
        with self.assertRaises(ValueError):
            booking_quote(1000, 2, 0, 10, 30)
        with self.assertRaises(ValueError):
            booking_quote(1000, 2, 1, -1, 30)
        with self.assertRaises(ValueError):
            booking_quote(1000, 2, 1, 10, 101)


if __name__ == "__main__":
    unittest.main()
