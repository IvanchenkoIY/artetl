import unittest

from src.route_price import balance_due


class BalanceTests(unittest.TestCase):
    def test_amount(self):
        self.assertEqual(balance_due(999, 299.7), 699.3)
        self.assertEqual(balance_due(0, 0), 0)
        self.assertEqual(balance_due(500, 500), 0)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            balance_due(100, -1)
        with self.assertRaises(ValueError):
            balance_due(100, 101)
        with self.assertRaises(ValueError):
            balance_due(-1, 0)


if __name__ == "__main__":
    unittest.main()
