#!/usr/bin/python3i
"""
Module file_storage serializes and
deserializes JSON types
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Custom Class for File Storage
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
         Returns dictionary representation of all objects
        """
        return self.__objects

    def new(self, obj):
        """"
        sets in __objects the object with the key
        <object class name>.id

        Args:
            object(obj): object to write
        """

        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
         serializes __objects to the JSON file
        (path: __file_path)

        """
        with open(self.__file_path, mode='w', encoding='utf-8') as file:
            obj_dict = {}
            for key, value in self.__objects.items():
                obj_dict[key] = value.to_dict()
            json.dump(obj_dict, file)

    def reload(self):
        """
        deserializes the JSON file to __objects, if the JSON
        file exists, otherwise nothing happens)

        """
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    cls_name, obj_id = key.split('.')
                    obj_cls = globals()[cls_name]
                    obj = obj_cls(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
