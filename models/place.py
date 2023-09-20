#!/usr/bin/python3

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

# Create the place_amenity association table for the Many-To-Many relationship
place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
)

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), nullable=False)
    user_id = Column(String(60), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)

    # Establish the Many-To-Many relationship with Amenity
    amenities = relationship("Amenity", secondary=place_amenity, back_populates="place_amenities")

    # Add getter and setter for amenities
    @property
    def amenities(self):
        """Getter attribute that returns the list of Amenity instances linked to this Place"""
        from models import storage
        all_amenities = storage.all("Amenity")
        linked_amenities = [amenity for amenity in all_amenities.values() if amenity.id in self.amenity_ids]
        return linked_amenities

    @amenities.setter
    def amenities(self, obj):
        """Setter attribute that appends an Amenity object's id to amenity_ids"""
        if obj.__class__.__name__ == "Amenity":
            self.amenity_ids.append(obj.id)
