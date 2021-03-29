#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Float, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship

place_amenity = Table('place_amenity', Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
        Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
)

class Place(BaseModel, Base):
    """ A place to stay """
    
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    
    reviews = relationship("Review", cascade="delete", backref='place')
    amenities = relationship("Amenity", secondary="place_amenity", viewonly=False)

    if getenv("HBNB_TYPE_STORAGE") != 'db':
        @property
        def reviews(self):
            """
            reviews getter
            """
            r_list = []
            r_all = models.storage.all(Review)
            for r in r_all.values():
                if r.state_id == self.id:
                    r_list.append(r)
            return r_list

        @property
        def amenities(self):
            """
            amenities getter
            """
            a_list = []
            for a in  models.storage.all(Amenity):
                if a.id in self.amenity_ids:
                    a_list.append(a)
            return a_list

        @amenities.setter
        def amenities(self, obj):
            """
            amenities getter
            """
            if type(obj) == Amenity:
                self.amenity_ids.append(obj.id)
