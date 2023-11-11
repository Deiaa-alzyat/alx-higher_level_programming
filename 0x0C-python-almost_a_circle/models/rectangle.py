#!/usr/bin/python3
"""Creating a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """The class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing the class Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """The width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting the width of the rectangle"""
        self.__width = value

    @property
    def height(self):
        """The height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting the height of the rectangle"""
        self.__height = value

    @property
    def x(self):
        """The x coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setting the x coordinate of the rectangle"""
        self.__x = value

    @property
    def y(self):
        """The y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setting the y coordinate of the rectangle"""
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        '''Method for validating the value.'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))


