#!/usr/bin/python3
""" First class Base """
import json
from os import path


class Base:
    """ Base """

    __nb__objects = 0

    def __init__(self, id=None):
        """ constructor initialization """
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
        return(json.dumps(list))

