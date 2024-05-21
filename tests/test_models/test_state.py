#!/usr/bin/python3

"""
Unit tests for the State class.
"""

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def test_instance_creation(self):
        """Test if an instance of State can be created."""
        state = State()
        self.assertIsInstance(state, State)

    def test_class_name(self):
        """Test the class name of the State instance."""
        state = State()
        self.assertEqual(str(type(state)), "<class 'models.state.State'>")

    def test_inheritance(self):
        """Test if State is a subclass of BaseModel."""
        state = State()
        self.assertTrue(issubclass(type(state), BaseModel))

    def test_attributes(self):
        """Test the attributes of the State instance."""
        state = State()
        self.assertIsNotNone(state.id)
        self.assertEqual(state.name, "")


if __name__ == "__main__":
    unittest.main()

