#!/usr/bin/python3
"""
This module defines a Square class
It checks value and type for its attributes
"""


class Square:
    """
    This is a square class
    """
    def __init__(self, size=0):
        """
        This function initializes a private variable size and has various exceptions for it
        """
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
