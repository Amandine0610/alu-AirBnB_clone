#!/usr/bin/python3

"""
Unit tests for the FileStorage class.
"""

import os
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorageInstantiation(unittest.TestCase):
    """
    Tests instantiation of the FileStorage class.
    """

    def test_file_storage_instantiation_no_args(self):
        self.assertIsInstance(FileStorage(), FileStorage)

    def test_file_storage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_file_storage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorageMethods(unittest.TestCase):
    """
    Tests methods of the FileStorage class.
    """

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn("User." + us.id, models.storage.all().keys())
        self.assertIn("State." + st.id, models.storage.all().keys())
        self.assertIn("Place." + pl.id, models.storage.all().keys())
        self.assertIn("City." + cy.id, models.storage.all().keys())
        self.assertIn("Amenity." + am.id, models.storage.all().keys())
        self.assertIn("Review." + rv.id, models.storage.all().keys())

    def test_save(self):
        bm = BaseModel()
        models.storage.new(bm)
        models.storage.save()
        with open("file.json", "r") as f:
            saved_data = f.read()
            self.assertIn("BaseModel." + bm.id, saved_data)

    def test_reload(self):
        bm = BaseModel()
        models.storage.new(bm)
        models.storage.save()
        models.storage.reload()
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())


if __name__ == "__main__":
    unittest.main()

