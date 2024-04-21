#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from models.base_model import Base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initializes a new City instance"""
        super().__init__(*args, **kwargs)  # Call superclass constructor

    def __str__(self):
        """Returns a string representation of the City instance"""
        return "[City] ({}) {}".format(self.id, self.name)
