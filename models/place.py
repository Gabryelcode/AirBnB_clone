#!/usr/bin/python3
"""Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place.
    Attributes:
        city_id (str): The ID of the city that the place is located in.
        user_id (str): The ID of the user who owns or manages the place.
        name (str): The name of the place.
        description (str): A Description of place.
        number_rooms (int): The number of rooms of the place.
        number_bathrooms (int): The number of bathrooms of the place.
        max_guest (int): The maximum number of guests
                        that the place can accommodate.
        price_by_night (int): The price per night of the place.
        latitude (float): The latitude coordinate of the place.
        longitude (float): The longitude coordinate of the place.
        amenity_ids (list): A list of the IDs of amenities
                            that are provided by the place.

    """

    city_id = ""

    user_id = ""

    name = ""

    description = ""

    number_rooms = 0

    number_bathrooms = 0

    max_guest = 0

    price_by_night = 0

    latitude = 0.0

    longitude = 0.0

    amenity_ids = []
