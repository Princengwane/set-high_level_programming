#!/usr/bin/python3
"""Defines the State model and the declarative Base."""
from sqlalchemy import Column, Integer, String

try:
    from sqlalchemy.orm import declarative_base
except ImportError:
    from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represent a state, mapped to the states table.

    Attributes:
        id (int): the state's primary key.
        name (str): the state's name.
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
