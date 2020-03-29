#!/usr/bin/python3
# class state
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """
    class City
    """

    __tablename__ = 'cities'
    id = Column(
            Integer,
            primary_key=True,
            unique=True,
            nullable=False,
            autoincrement="auto"
        )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
