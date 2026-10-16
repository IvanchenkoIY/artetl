import unittest

from src.route_price import stay_total


class StayTests(unittest.TestCase):
    def test_amount(self):
        self.assertEqual(stay_total(1200, 2, 3), 7200)
        self.assertEqual(stay_total(10.55, 3), 31.65)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            stay_total(-1, 1)
        with self.assertRaises(ValueError):
            stay_total(10, 0)
        with self.assertRaises(ValueError):
            stay_total(10, 1, 0)
        with self.assertRaises(ValueError):
            stay_total(10, True)
        with self.assertRaises(ValueError):
            stay_total(10, 1, True)


if __name__ == "__main__":
    unittest.main()
