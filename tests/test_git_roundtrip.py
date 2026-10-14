import unittest
from src.git_roundtrip import greet


class GreetingTests(unittest.TestCase):
    def test_name(self):
        self.assertEqual(greet("Alice"), "Hi, Alice!")

    def test_trim(self):
        self.assertEqual(greet("  Bob  "), "Hi, Bob!")

    def test_blank_name(self):
        self.assertEqual(greet("   "), "Hi, world!")
