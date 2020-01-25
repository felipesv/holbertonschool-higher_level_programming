#!/usr/bin/python3
"""
class Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle
    """

    def __init__(self, width, height):
        """
        constructor
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        get the area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        get the size
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
