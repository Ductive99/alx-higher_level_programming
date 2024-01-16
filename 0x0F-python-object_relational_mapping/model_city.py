#!/usr/bin/python3
"""
Module that defines the `City` class
That inherits from Base (imported from model_state)
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """
    City Class

    id: auto-generated, unique integer (can't be null)
        is a primary key
    name: string of 128 characters     (can't be null)
    state_id: foreign key to states.id (can't be null)
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
