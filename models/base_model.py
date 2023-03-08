#!/usr/bin/python3
import uuid
import datetime
"""
 Class that serves as a template for creating other model classes.

"""


class BaseModel():
        
    date_format = "%Y-%m-%dT%H:%M:%S.%f"
    def __init__(self, *args, **kwargs):
        """ initializes the instance """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at
        
        for key, value in kwargs.items():
            if key == '__class__':
                continue
            if key == 'created_at' or key == 'updated_at':
                value = datetime.datetime.strptime(value,"%Y-%m-%dT%H:%M:%S.%f")
            setattr(self,key,value)

    def __str__(self):
        """
        method is defined to return a string representation of the instance """
        return (f"[{type(self).__name__}] ({self.id}) ({self.__dict__})")

    def save(self):
        """  update the the instance with current time """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns the dictionary representation of the instance """
        result = self.__dict__.copy()
        result['__class__'] = type(self).__name__
        result['created_at'] = self.created_at.strftime(self.date_format)
        result['updated_at'] = self.updated_at.strftime(self.date_format)
        return result
