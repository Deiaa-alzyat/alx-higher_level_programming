#!/usr/bin/python3
"""Base class"""
import csv
from json import dumps, loads


class Base:
    """Definition"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Jsonifies a dictionary so it's quite rightly and longer.'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Saves jsonified object to file.'''
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        '''Unjsonifies a dictionary.'''
        if json_string is None or not json_string:
            return []
        return loads(json_string)
