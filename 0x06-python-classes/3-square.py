#!/usr/bin/python3
"""
This module defines a Square class
Its implements value and type checks for its attributes and variables
"""


class Square:
    """This is a square class as defined
    """
    def __init__(self, size=0):
        """This function checks value and type checks and also defines a private instance attribute"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """This function returns the current square area defined"""
        return (self.__size ** 2)
