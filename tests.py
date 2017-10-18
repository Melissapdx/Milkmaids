from unittest import TestCase
from server import app
from flask import session
from model import db, example_dat, connect_to_db


class Milktests(TestCase):
    """Tests for milkmaid site"""

    def setUp(self):
        """Basic test setup"""
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Test homepage"""
        result = self.client.get('/')
        self.assertIn("<title>Milkmaids</title>", result.data)

    def test_login_elements(self):
        """ Test Login page elements"""
        result = self.client.get('/login')
        self.assertIn("<h2>Sign In</h2>", result.data)
        self.assertIn("<h2>Create an Account</h2>", result.data)

    def test_shop(self):
        """Test shop page"""
        self.client.post("/shop", follow_redirects=True)

    def test_cart(self):
        """Test shop page"""
        self.client.post("/cart", follow_redirects=True)


class FlaskTestsDatabase(TestCase):

    def setUp(self):
        """Basic test setup"""
        # Connect to test database
        connect_to_db(app, "postgresql:///testdb")
        # Create tables and add sample data
        db.create_all()
        example_data()

    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        db.drop_all()

    def test_user_login(self):
        """Test user login"""
        result = self.client.post("/login",
            data={"email_2": "SusanSnow@gmail.com",
            "password_2": "1234"},
            follow_redirects=True)


if __name__ == "__main__":
    import unittest
    unittest.main()
