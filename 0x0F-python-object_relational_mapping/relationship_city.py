#!/usr/bin/python3

"""
   contains the class definition of a City
"""
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


# Define a model class for the "City" table
class City(Base):
    """City class, inherits from Base (SQLAlchemy)
    class attributes:
        id -> auto generated integer
        name -> non nullable string
        state_id -> non nullable integer
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State")
