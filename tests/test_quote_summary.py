import unittest

from src.route_price import booking_quote, quote_summary


class SummaryTests(unittest.TestCase):
    def test_totals(self):
        q = booking_quote(1000, 2, 1, 10, 30)
        s = quote_summary([q, q])
        self.assertEqual(s["count"], 2)
        self.assertEqual(s["total"], 3600)
        self.assertEqual(s["deposit"], 1080)
        self.assertEqual(s["balance"], 2520)

    def test_empty(self):
        s = quote_summary([])
        self.assertEqual(s["count"], 0)
        self.assertEqual(s["total"], 0)
        self.assertEqual(s["deposit"], 0)
        self.assertEqual(s["balance"], 0)


if __name__ == "__main__":
    unittest.main()
