import unittest
from src.git_roundtrip import greet


class GreetingTests(unittest.TestCase):
    def test_name(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")

    def test_trim(self):
        self.assertEqual(greet("  Bob  "), "Hello, Bob!")
