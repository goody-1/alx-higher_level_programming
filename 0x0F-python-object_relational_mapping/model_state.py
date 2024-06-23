#!/usr/bin/python3

"""
    contains the class definition of a State and an instance
    Base
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# Create a base class for declarative models
Base = declarative_base()


# Define a model class for the "State" table
class State(Base):
    """State class, inherits from Base (SQLAlchemy)
    class attributes:
        id -> auto generated integer
        name -> non nullable string
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
