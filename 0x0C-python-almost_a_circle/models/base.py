#!/usr/bin/python3
"""Base class"""
import json
import csv


class Base:
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
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
        """new instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """ist of instances"""
        _file = cls.__name__ + ".json"

        try:
            _list = []
            with open(_file, mode="r", encoding="utf-8") as file:
                _dict = cls.from_json_string(file.read())
            for i in _dict:
                _list.append(cls.create(**i))
            return _list
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Same as JSON but with cvs
        """
        csvfile = '{}.csv'.format(cls.__name__)
        with open(csvfile, 'w', newline='') as csvf:
            if list_objs is None or list_objs == []:
                csvf.write('[]')
            else:
                if cls.__name__ == 'Square':
                    fields = ["id", "size", "x", "y"]
                else:
                    fields = ["id", "width", "height", "x", "y"]
                doc = csv.DictWriter(csvf, fieldnames=fields)
                [doc.writerow(inst.to_dictionary()) for inst in list_objs]

    @classmethod
    def load_from_file_csv(cls):
        """
        Same as JSON but with cvs
        """
        csvfile = '{}.csv'.format(cls.__name__)
        try:
            with open(csvfile, 'r', newline='') as csvf:
                if cls.__name__ == 'Square':
                    fields = ["id", "size", "x", "y"]
                else:
                    fields = ["id", "width", "height", "x", "y"]
                doc = csv.DictReader(csvf, fieldnames=fields)
                ls_of_dics = [{k: int(v) for k, v in dic.items()}
                              for dic in doc]
                return [cls.create(**dics) for dics in ls_of_dics]
        except IOError:
            return []
