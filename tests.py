from unittest import TestCase
from server import app
from flask import session


class Milktests(TestCase):
    """Tests for milkmaid site"""

    def setUp(self):
        print "started setup"
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        print self
        result = self.client.get('/')
        self.assertIn("<title>Milkmaids</title>", result.data)

if __name__ == "__main__":
    import unittest
    unittest.main()
