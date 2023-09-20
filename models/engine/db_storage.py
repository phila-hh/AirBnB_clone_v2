#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class DBStorage:
    """This class manages storage of hbnb models in MYSQL databases"""
    __engine__ = None
    __session__ = None
    def __init__(self):
        """Initializes the DBStorage engine"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.
                                        format(getenv('HBNB_MYSQL_USER'),
                                               getenv('HBNB_MYSQL_PWD'),
                                               getenv('HBNB_MYSQL_HOST'),
                                               getenv('HBNB_MYSQL_DB')))
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query and return all objects of a specified class or all classes"""
        obj_dict = {}
        if cls:
            query_objs = self.__session.query(cls).all()
            for obj in query_objs:
                key = "{}.{}".format(cls.__name__, obj.id)
                obj_dict[key] = obj
        else:
            for cls in [User, State, City, Amenity, Place, Review]:
                query_objs = self.__session.query(cls).all()
                for obj in query_objs:
                    key = "{}.{}".format(cls.__name__, obj.id)
                    obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
       """Commit all changes to the current database session"""
       self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and create the current database session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        DBStorage.__session = scoped_session(session_factory)

    def close(self):
        """Closes the current session"""
        self.__session.remove() 
