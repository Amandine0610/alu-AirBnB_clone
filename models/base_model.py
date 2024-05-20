#!/usr/bin/python3
"""This script  defines the BaseModel class, the foundation for other models."""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """A base class for all models in our application."""

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of BaseModel.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            now = datetime.now()
            self.created_at = now
            self.updated_at = now
            storage.new(self)

    def __str__(self):
        """
        Return a string representation of the instance.
        """
        cls_name = type(self).__name__
        return f"[{cls_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update 'updated_at' with the current datetime and save the instance."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        convert the instance to a dictionary.
        """
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = type(self).__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        return instance_dict

