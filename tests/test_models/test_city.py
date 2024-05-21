#!/usr/bin/python3

"""
Unit tests for the City class.
"""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_instance_creation(self):
        """Test if an instance of City can be created."""
        city = City()
        self.assertIsInstance(city, City)

    def test_class_name(self):
        """Test the class name of the City instance."""
        city = City()
        self.assertEqual(str(type(city)), "<class 'models.city.City'>")

    def test_inheritance(self):
        """Test if City is a subclass of BaseModel."""
        city = City()
        self.assertTrue(issubclass(type(city), BaseModel))

    def test_default_name(self):
        """Test the default value of the 'name' attribute."""
        city = City()
        self.assertEqual(city.name, "")

    def test_default_state_id(self):
        """Test the default value of the 'state_id' attribute."""
        city = City()
        self.assertEqual(city.state_id, "")


if __name__ == "__main__":
    unittest.main()

