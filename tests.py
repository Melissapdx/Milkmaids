from unittest import TestCase
from server import app
from flask import session
from model import db, example_data, connect_to_db


class Milktests(TestCase):
    """Tests routes for Milkmaids site"""

    def setUp(self):
        """Basic test setup"""
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Test homepage"""
        result = self.client.get('/')
        self.assertIn("<title>Milkmaids</title>", result.data)
        self.assertIn("<h2>About</h2>", result.data)

    def test_login_elements(self):
        """ Test Login page elements"""
        result = self.client.get('/login')
        self.assertIn("<h2>Sign In</h2>", result.data)
        self.assertIn("<h2>Create an Account</h2>", result.data)

    def test_cart(self):
        """Test cart page"""
        result = self.client.get("/cart")
        self.assertEqual(result.status_code, 200)


class FlaskTestsDatabase(TestCase):

    def setUp(self):
        """Basic test setup"""
        self.client = app.test_client()
        app.config['TESTING'] = True
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
                    data={"email_2": "person@gmail.com",
                    " password_2": "admin"},
                    follow_redirects=True)
        self.assertEqual(result.status_code, 200)

    def test_shop(self):
        """Test shop page"""
        result = self.client.get("/shop")
        self.assertEqual(result.status_code, 200)

    def logout(self):
        """Test logout page"""
        result = self.client.get("/logout")
        self.assertEqual(result.status_code, 200)

    def register(self):
        """Test registration page"""
        result = self.client.get("/register")
        self.assertEqual(result.status_code, 200)

if __name__ == "__main__":
    import unittest
    unittest.main()
