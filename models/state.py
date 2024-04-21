#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from os import getenv
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from models.base_model import Base
import models


class State(BaseModel, Base):
    """ State class """
    if models.storage_t == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City",  backref="state", cascade="delete")
    else:
        name = ""
    

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)



    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """ new method """
            cs = []
            for tw in list(models.storage.all(City).values()):
                if tw.state_id == self.id:
                    cs.append(tw)
            return cs
