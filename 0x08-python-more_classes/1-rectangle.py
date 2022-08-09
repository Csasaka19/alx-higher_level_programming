#!/usr/bin/python3
"""
This module defines the a Rectangle Object.
"""


class Rectangle:
    """Retangle class that has getters,setters and properties
    """
    def __init__(self, width=0, height=0):
        """Function that defines weight and width public instances"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Function retrives the private attribute width via a property"""
        return self.__width

    @width.setter
    def width(self, value):
        """Function that checks for type and value of the width attribute"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Function retrives the private attribute height via a property"""
        return self.__height

    @height.setter
    def height(self, value):
        """Function that checks for type and value of the height attribute"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
