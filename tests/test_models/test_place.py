#!/usr/bin/python3

"""
Unit tests for the Place class.
"""

import unittest
from models.place import Place
from models.city import City
from models.user import User
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def test_instance_creation(self):
        """Test if an instance of Place can be created."""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_class_name(self):
        """Test the class name of the Place instance."""
        place = Place()
        self.assertEqual(str(type(place)), "<class 'models.place.Place'>")

    def test_inheritance(self):
        """Test if Place is a subclass of BaseModel."""
        place = Place()
        self.assertTrue(issubclass(type(place), BaseModel))

    def test_attributes(self):
        """Test the attributes of the Place instance."""
        city = City()
        user = User()
        place = Place()
        place.user_id = user.id
        place.city_id = city.id
        self.assertIsNotNone(place.id)
        self.assertEqual(place.user_id, user.id)
        self.assertEqual(place.city_id, city.id)
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0)
        self.assertEqual(place.longitude, 0)
        self.assertEqual(place.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()

