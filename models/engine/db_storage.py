#!/usr/bin/python3
""" import models """

from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv

class DBStorage:
    """ db class new"""
    __engine = None
    __session =  None
    def __init__(self):
        self.engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            getenv("HBNB_MYSQL_USER"),
            getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"),
            getenv("HBNB_MYSQL_DB")),  pool_pre_ping=True)
        if (getenv("HBNB_ENV") == "test"):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ new method """
        if cls != None:
            if type(cls) == str:
                cls = eval(cls)
            dic = self.__session.query(cls)
        else:
            dic = self.__session.query(State).all()
            dic.extend(self.__session.query(Amenity).all())
            dic.extend(self.__session.query(Review).all())
            dic.extend(self.__session.query(Place).all())
            dic.extend(self.__session.query(User).all())
            dic.extend(self.__session.query(City).all())

        return {"{}.{}".format(type(i).__name__, i.id): i for i in dic}

    def new(self, obj):
        """ new method """
        self.__session.add(obj)

    def save(self):
        """ new method """
        self.__session.commit()

    def delete(self, obj=None):
        """ new method """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ new method """
        Base.metadata.create_all(self.__engine)
        s = sessionmaker(bind=self.__engine,expire_on_commit=False)
        a = scoped_session(s)
        self.__session = a()


    def close(self):
        """ new method flask"""
        self.__session.remove()
