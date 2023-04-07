#!/usr/bin/python3
"""
Place class, a subclass of BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):

    """
    Inherits from BaseModel class

       Attributes:

         city_id: string -  City.id
         user_id: string -  User.id
         name: string
         description:  string
         number_rooms: integer
         number_bathrooms: integer
         max_guest: integer
         price_by_night: integer
         latitude: float
         longitude: float
         amenity_ids: list of string - Amenity.id later
     """
    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = float(0)
    longitude = float(0)
    amenity_ids = []
