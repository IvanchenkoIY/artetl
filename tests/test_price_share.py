import unittest

from src.route_price import per_person


class ShareTests(unittest.TestCase):
    def test_three_people(self):
        self.assertEqual(per_person(100, 3), 33.33)

    def test_invalid_people(self):
        with self.assertRaises(ValueError):
            per_person(100, 0)
        with self.assertRaises(ValueError):
            per_person(100, -1)


if __name__ == "__main__":
    unittest.main()
