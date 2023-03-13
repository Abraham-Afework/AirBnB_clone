#!/usr/bin/python3
import json
from models.base_model import BaseModel



class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):

        return self.__objects
    def new(self, obj):

        self.__objects[obj.__class__.__name__ + '.'+ obj.id]  = obj
    
    def save(self):

        with open(self.__file_path, 'a+') as f:
            for key, value in self.__objects.items():
                    json.dump({key: value.to_dict()},f)
    
    def reload(self):
        try:
            with open(self.__file_path,'r') as f:
                json_file = json.loads(f.read())
                for value in json_file.value():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except Exception:
            pass

