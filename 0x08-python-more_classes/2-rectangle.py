#!/usr/bin/python3
"""
This module defines the a Rectangle Object, it has six functions
"""


class Rectangle:
    """Retangle object with prroperties, getters and setters
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Function retrives the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Function tests type and value of the width instance"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Function retrives the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Function tests type and value of the height instance"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Function returns current area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Function returns current perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))
