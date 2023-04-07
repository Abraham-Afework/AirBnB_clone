#!/usr/bin/python3
"""user class, subclass of BaseModel
"""

from models.base_model import BaseModel
import json


class User(BaseModel):

    """
    Represent a User
         Attributes:
             email (str): user email
             password (str): user password
             first_name (str): first name
             last_name (str): last name """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
