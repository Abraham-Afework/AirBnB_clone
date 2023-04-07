#!/usr/bin/python3
"""
City class, a subclass of BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):

    """
    A subclass of BaseModel class
    Public class attribute:
        name: (str)
        state_id: (str)
    """
    name = ""
    state_id = ""
