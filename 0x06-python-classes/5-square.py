#!/usr/bin/python3
"""
This module defines a Square class
Its implements value and type checks for its attributes
The class also uses properties to state various instances
"""


class Square:
    """This is a square class declaration
    """
    def __init__(self, size=0):
        """This function is a Instantiation with option"""
        self.__size = size

    @property
    def size(self):
        """This function retrives the private attribute through a property"""
        return self.__size

    @size.setter
    def size(self, size):
        """This function checks value and type of the private instance through a property setter"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """This function returns the current square area
        """
        return (self.__size ** 2)

    def my_print(self):
        """This funtion prints a square  with the exact size except when the value is 0
        """
        if (self.__size == 0):
            print('')

        for l in range(self.__size):
            print('#' * self.__size)
