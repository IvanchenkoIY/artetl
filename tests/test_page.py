import unittest
from src.page import render_page

class PageTests(unittest.TestCase):
    def test_description(self):
        html = render_page()
        self.assertIn('Конжаковский Камень', html)
        self.assertIn('viewport', html)
        self.assertIn('<style>', html)
        self.assertIn('О походе', html)
        self.assertIn('Подготовка', html)
        self.assertIn('Запись', html)
        self.assertIn('lang="ru"', html)

    def test_form_and_success(self):
        html = render_page()
        self.assertIn('method="post"', html)
        self.assertIn('action="/register"', html)
        self.assertIn('name="name"', html)
        self.assertIn('maxlength="80"', html)
        self.assertIn('name="email"', html)
        self.assertIn('type="email"', html)
        self.assertIn('maxlength="254"', html)
        self.assertIn('Записаться', html)
        self.assertIn('Учебный сайт', html)
        self.assertNotIn('Заявка принята', html)
        html_ok = render_page(True)
        self.assertIn('Заявка принята', html_ok)
        self.assertNotIn('example.test', html_ok)
