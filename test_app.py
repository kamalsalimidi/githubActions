import unittest
from app import message

class MessageTests(unittest.TestCase):
    def test_greeting(self):
        self.assertEqual(message()["message"], "Hello trainee example")

    def test_version(self):
        self.assertEqual(message()["version"], "1.0")

if __name__ == "__main__":
    unittest.main()
