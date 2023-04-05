#!/usr/bin/python3
from models.base_model import BaseModel


class Place(BaseModel):

		name = ""
		city_id = ""
		user_id = ""
		description = ""
		number_rooms = 0
		number_bathrooms = 0
		max_guest = 0
		price_by_night = 0
		lattitude = float(0)
		longtiude = float(0)
		amenity_ids = []

