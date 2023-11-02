#!/usr/bin/python3
"""
Defines a city class
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model_city import Base, City

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete-orphan")
