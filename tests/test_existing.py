import unittest
from src.quote import quote

class Existing(unittest.TestCase):
    def test_regular(self):
        self.assertEqual(quote(2, 3), 6000)
