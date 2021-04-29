#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Representation of state """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="delete", backref='state')

    if getenv("HBNB_TYPE_STORAGE") != 'db':
        @property
        def cities(self):
            c_list = []
            c_all = models.storage.all(City)
            for c in c_all.values():
                if c.state_id == self.id:
                    c_list.append(c)
            return c_list
