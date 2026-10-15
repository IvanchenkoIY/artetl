import os
import sqlite3
import tempfile
import unittest

from src.registration import register


class RegistrationTests(unittest.TestCase):
    def setUp(self):
        fd, self.db_path = tempfile.mkstemp(suffix=".db")
        os.close(fd)
        conn = sqlite3.connect(self.db_path)
        try:
            conn.execute("CREATE TABLE IF NOT EXISTS registrations (name TEXT, email TEXT)")
            conn.commit()
        finally:
            conn.close()

    def tearDown(self):
        if os.path.exists(self.db_path):
            os.unlink(self.db_path)

    def test_persistence(self):
        self.assertIsNone(register(self.db_path, "  Anna  ", "anna@example.test"))
        self.assertIsNone(register(self.db_path, "Boris", "boris@example.test"))

        conn = sqlite3.connect(self.db_path)
        try:
            rows = conn.execute("SELECT name, email FROM registrations ORDER BY rowid").fetchall()
        finally:
            conn.close()

        self.assertEqual(rows, [("Anna", "anna@example.test"), ("Boris", "boris@example.test")])

    def test_invalid(self):
        bad_inputs = [
            ("A", "ok@example.test"),
            ("x" * 81, "ok@example.test"),
            ("Anna", ""),
            ("Anna", "no-at-sign"),
            ("Anna", "a@@example.test"),
            ("Anna", "@example.test"),
            ("Anna", "anna@"),
            ("Anna", "anna@nodot"),
            ("Anna", "anna @example.test"),
            ("Anna", "anna\t@example.test"),
            ("Anna", "anna\x01@example.test"),
            ("Anna", "a" * 255 + "@example.test"),
        ]
        for name, email in bad_inputs:
            with self.assertRaises(ValueError):
                register(self.db_path, name, email)

        conn = sqlite3.connect(self.db_path)
        try:
            count = conn.execute("SELECT COUNT(*) FROM registrations").fetchone()[0]
        finally:
            conn.close()
        self.assertEqual(count, 0)


if __name__ == "__main__":
    unittest.main()
