#!/usr/bin/python3
""" First class Base """


import json

from os import path


class Base:
    """Base"""

    __nb__objects = 0

    def __init__(self, id=None):
        """constructor initialization"""
        if id is not None:
            self.id = id

        else:
            Base.__nb__objects += 1
            self.id = Base.__nb__objects

    @staticmethod
    def to_json_string(list_dictionaries):
        list = []
        if list_dictionaries:
            for element in list_dictionaries:
                list.append(element)
        return json.dumps(list)

    @classmethod
    def save_to_file(cls, list_objs):
        list2 = []
        with open("{}.json".format(cls.__name__), "w") as file:
            if list_objs:
                for obj in list_objs:
                    obj_dict = obj.to_dictionary()
                    list2.append(obj_dict)
            file.write(cls.to_json_string(list2))

    @staticmethod
    def from_json_string(json_string):
        if json_string:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        list4 = []
        try:
            with open("{}.json".format(cls.__name__), "r") as file:
                str_list = file.read()
            dict_list = cls.from_json_string(str_list)
        except:
            dict_list = dict()
        for obj_dict in dict_list:
            new_obj = cls.create(**obj_dict)
            list4.append(new_obj)
        return list4
