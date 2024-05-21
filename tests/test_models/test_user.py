#!/usr/bin/python3

"""
Unit tests for the User class.
"""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def test_instance_creation(self):
        """Test if an instance of User can be created."""
        user = User()
        self.assertIsInstance(user, User)

    def test_class_name(self):
        """Test the class name of the User instance."""
        user = User()
        self.assertEqual(str(type(user)), "<class 'models.user.User'>")

    def test_inheritance(self):
        """Test if User is a subclass of BaseModel."""
        user = User()
        self.assertTrue(issubclass(type(user), BaseModel))

    def test_id_generation(self):
        """Test the generation of the 'id' attribute."""
        user = User()
        self.assertIsNotNone(user.id)

    def test_email_attribute(self):
        """Test the 'email' attribute of the User instance."""
        user = User()
        self.assertEqual(user.email, "")
        user.email = "airbnb@mail.com"
        self.assertEqual(user.email, "airbnb@mail.com")

    def test_password_attribute(self):
        """Test the 'password' attribute of the User instance."""
        user = User()
        self.assertEqual(user.password, "")
        user.password = "root"
        self.assertEqual(user.password, "root")

    def test_first_name_attribute(self):
        """Test the 'first_name' attribute of the User instance."""
        user = User()
        self.assertEqual(user.first_name, "")
        user.first_name = "Betty"
        self.assertEqual(user.first_name, "Betty")

    def test_last_name_attribute(self):
        """Test the 'last_name' attribute of the User instance."""
        user = User()
        self.assertEqual(user.last_name, "")
        user.first_name = "Bar"
        self.assertEqual(user.first_name, "Bar")


if __name__ == "__main__":
    unittest.main()

