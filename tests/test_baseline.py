import unittest
from src.page import render_page
from src.registration import register

class Baseline(unittest.TestCase):
    def test_contract_exists(self):
        self.assertTrue(callable(register))
        self.assertIsInstance(render_page(), str)
