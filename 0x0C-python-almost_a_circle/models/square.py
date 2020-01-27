#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get size"""
        return self.width

    @size.setter
    def size(self, value):
        """set size"""
        self.width = value
        self.height = value

    def __str__(self):
        """str method"""
        _str1 = "[Square] ({}) ".format(self.id)
        _str2 = "{}/{} - ".format(self.x, self.y)
        _str3 = "{}".format(self.width)

        return _str1 + _str2 + _str3

    def update(self, *args, **kwargs):
        """update class"""
        if args:
            _key = ["id", "size", "x", "y"]
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
        _key = ["id", "size", "x", "y"]
        _val = []
        for i in _key:
            _val.append(getattr(self, i))
        _dict = dict(zip(_key, _val))

        return _dict
