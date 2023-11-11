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

