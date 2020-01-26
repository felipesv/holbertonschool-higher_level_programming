#!/usr/bin/python3
"""Base class"""
import json


class Base:
        """Base Class"""
        __nb_objects = 0

        def __init__(self, id=None):
                """Constructor"""
                self.__nb_objects = 0

                if id is None:
                        Base.__nb_objects += 1
                        self.id = Base.__nb_objects
                else:
                        self.id = id

        def to_json_string(list_dictionaries):
                """SON string representation of list_dictionaries"""
                if not list_dictionaries or list_dictionaries is None:
                        return "[]"
                return json.dumps(list_dictionaries)

        @classmethod
        def save_to_file(cls, list_objs):
                """JSON string representation of list_objs to a file"""
                _file = cls.__name__ + ".json"

                with open(_file, mode="w") as file:
                        _dict = [i.to_dictionary() for i in list_objs]
                        file.write(cls.to_json_string(_dict))

        @staticmethod
        def from_json_string(json_string):
                """JSON string to list"""
                if not json_string or json_string is None:
                        return []
                return json.loads(json_string)

        @classmethod
        def create(cls, **dictionary):
                if cls.__name__ == "Rectangle":
                        new = cls(1, 1)
                else:
                        new = cls(1)
                new.update(**dictionary)
                return new

        @classmethod
        def load_from_file(cls):
                _file = cls.__name__ + ".json"

                try:
                        pass
                except Exception:
                        return []
                        
