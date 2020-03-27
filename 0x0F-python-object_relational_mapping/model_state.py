#!/usr/bin/python3
# class state
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    class State
    """

    __tablename__ = 'state'
    id = Column(
            Integer,
            primary_key=True,
            nullable=False,
            autoincrement="auto"
        )
    name = Column(String(128), nullable=False)
