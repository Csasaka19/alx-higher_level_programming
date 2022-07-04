#!/usr/bin/python3
"""
This module implements a Square object subclass
that inherits from the rectangle superclass
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """initialization
        Args:
            size (int): size
        """
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns: area"""
        return self.__size * self.__size

    def __str__(self):
        """Return: string
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
