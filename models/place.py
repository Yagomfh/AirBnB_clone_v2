#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Float, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

metadata = Base.metadata
association_table = Table('place_amenity', metadata,
        Column('place_id', ForeignKey('places.id'), String(60), primary_key=True, nullable=False),
        Column('amenity_id', ForeignKey('amenities.id'), String(60), primary_key=True, nullable=False)
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
    amenities = relationship("Amenity", secondary=association_table, viewonly=False)

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
            a_all = models.storage.all(Amenity)
            for a in a_all.values():
                if a.place_id == self.id:
                    a_list.append(a.id)
            return a_list

        @amenities.setter
        def amenities(self, obj):
            """
            amenities getter
            """
            if obj is type(Amenity):
                amenity_ids.append(obj.id)
