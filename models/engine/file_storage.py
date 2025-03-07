#!/usr/bin/python3
"""
This module defines a class to manage file storage for hbnb clone
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {"BaseModel": BaseModel,
           "User": User,
           "Place": Place,
           "State": State,
           "City": City,
           "Amenity": Amenity,
           "Review": Review}


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            new_objs = {}
            for key, value in self.__objects.items():
                if isinstance(value, cls):
                    new_objs[key] = value
            return new_objs
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                djo = json.load(f)
            for key in djo:
                self.__objects[key] = a_dict[djo[key]['__class__']](**djo[key])
        except:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if it’s inside else do nothing """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """Method for deserializing the JSON file to objects"""
        self.reload()
