import unittest

from route_price import deposit_amount


class DepositTests(unittest.TestCase):
    def test_amount(self):
        self.assertEqual(deposit_amount(999, 30), 299.7)
        self.assertEqual(deposit_amount(10.55, 15), 1.58)
        self.assertEqual(deposit_amount(100, 0), 0)
        self.assertEqual(deposit_amount(100, 100), 100)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            deposit_amount(-1, 10)
        with self.assertRaises(ValueError):
            deposit_amount(100, -1)
        with self.assertRaises(ValueError):
            deposit_amount(100, 101)


if __name__ == "__main__":
    unittest.main()
