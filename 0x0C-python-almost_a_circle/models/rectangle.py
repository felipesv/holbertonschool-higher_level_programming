#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set heigth"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """get area"""
        return self.__width * self.__height

    def display(self):
        """display rectangle"""
        for j in range(self.__y):
            print("")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """str method"""
        _str1 = "[Rectangle] ({}) ".format(self.id)
        _str2 = "{}/{} - ".format(self.__x, self.__y)
        _str3 = "{}/{}".format(self.__width, self.__height)
        return _str1 + _str2 + _str3

    def update(self, *args, **kwargs):
        """update class"""
        if args:
            _key = ["id", "width", "height", "x", "y"]
            _val = list(args)
            _dic = {}
            for i in range(len(_val)):
                _dic[_key[i]] = _val[i]

            for key, value in _dic.items():
                setattr(self, key, value)
            return
        if kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
            return

    def to_dictionary(self):
        """get attr in dict"""
        _key = ["id", "width", "height", "x", "y"]
        _val = []
        for i in _key:
            _val.append(getattr(self, i))
        _dict = dict(zip(_key, _val))

        return _dict
