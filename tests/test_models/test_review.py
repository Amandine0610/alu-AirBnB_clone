#!/usr/bin/python3

"""
Unit tests for the Review class.
"""

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def test_instance_creation(self):
        """Test if an instance of Review can be created."""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_class_name(self):
        """Test the class name of the Review instance."""
        review = Review()
        self.assertEqual(str(type(review)), "<class 'models.review.Review'>")

    def test_inheritance(self):
        """Test if Review is a subclass of BaseModel."""
        review = Review()
        self.assertTrue(issubclass(type(review), BaseModel))

    def test_attributes(self):
        """Test the attributes of the Review instance."""
        review = Review()
        self.assertIsNotNone(review.id)
        self.assertEqual(review.text, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.place_id, "")


if __name__ == "__main__":
    unittest.main()

