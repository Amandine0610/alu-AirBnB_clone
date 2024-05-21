#!/usr/bin/python3

"""Unit tests for the Amenity class."""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test suite for the Amenity class."""

    def test_instance_creation(self):
        """Test if an Amenity instance is correctly created."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_class_type(self):
        """Test if the instance is of the correct class type."""
        amenity = Amenity()
        self.assertEqual(str(type(amenity)),
                         "<class 'models.amenity.Amenity'>")

    def test_inheritance(self):
        """Test if Amnity is a subclass of BaseModel."""
        amenity = Amenity()
        self.assertTrue(issubclass(type(amenity), BaseModel))

    def test_default_attributes(self):
        """Test the default attributes of an amenity instance."""

        amenity = Amenity()
        self.assertEqual(amenity.name, "")
        self.assertIsNotNone(amenity.id)


if __name__ == "__main__":
    unittest.main()

