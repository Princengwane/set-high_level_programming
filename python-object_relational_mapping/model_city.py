#!/usr/bin/python3
"""Defines the City model, linked to the states table."""
from model_state import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class City(Base):
    """Represent a city, mapped to the cities table.

    Attributes:
        id (int): the city's primary key.
        name (str): the city's name.
        state_id (int): the id of the state the city belongs to.
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
