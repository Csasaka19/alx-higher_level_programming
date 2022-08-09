#!/usr/bin/python3
"""
This module defines a Square class
Its implements value and type checks for its attributes and has an area function
It has four functions
"""


class Square:
    """This is a square class defined
    """
    def __init__(self, size=0):
        """This function uses instantiation with option"""
        self.size = size

    @property
    def size(self):
        """This function uses the property to retrive the private attribute size"""
        return self.__size

    @size.setter
    def size(self, size):
        """This function uses a property setter to set the private attribute size"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """This function returns the current area of the defined square"""
        return (self.__size ** 2)
