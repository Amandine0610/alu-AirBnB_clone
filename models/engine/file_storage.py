#!/usr/bin/python3
"""Module for FileStorage class."""

import json
import os
from datetime import datetime


class FileStorage:
    """A class that serializes instances to a JSON file and deserializes JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Add the object to the __objects dictionary."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump({key: obj.to_dict() for key, obj in self.__objects.items()}, file)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    cls_name = value["__class__"]
                    self.__objects[key] = self.classes()[cls_name](**value)

    def classes(self):
        """Return a dictionary of valid classes and their references."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        return {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

    def attributes(self):
        """Return the valid attributes and their types for each class."""
        return {
            "BaseModel": {
                "id": str,
                "created_at": datetime,
                "updated_at": datetime
            },
            "User": {
                "email": str,
                "password": str,
                "first_name": str,
                "last_name": str
            },
            "State": {
                "name": str
            },
            "City": {
                "state_id": str,
                "name": str
            },
            "Amenity": {
                "name": str
            },
            "Place": {
                "city_id": str,
                "user_id": str,
                "name": str,
                "description": str,
                "number_rooms": int,
                "number_bathrooms": int,
                "max_guest": int,
                "price_by_night": int,
                "latitude": float,
                "longitude": float,
                "amenity_ids": list
            },
            "Review": {
                "place_id": str,
                "user_id": str,
                "text": str
            }
        }

