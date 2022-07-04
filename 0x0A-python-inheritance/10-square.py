#!/usr/bin/python3
"""
This module implements a Square object subclass
that inherits from the superclass Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """implementation
    """
    def __init__(self, size):
        """initialization
        Args: size
        """
        super().__init__(size, size)
        self.__size = size
   
    def area(self):
        """Returns area"""
        return self.__size * self.__size
