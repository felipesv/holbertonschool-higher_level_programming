#!/usr/bin/python3
"""
Class to create a rectangle
"""


class Rectangle:
    """
    Class to create a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        constructor
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        get the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set the width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        get the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        set the height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
