#!/usr/bin/python3
"""
This module defines a Square class
Its implements value and type checks for its attributes
Attributes in this module:
    area
    position
    size
    my_print
"""


class Square:
    """This is a square class definition
    """
    def __init__(self, size=0, position=(0, 0)):
        """This function shows public instances of position and size"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """This function retrives private size by a property"""
        return self.__size

    @size.setter
    def size(self, size):
        """This function tests type and value of the private instance using a property setter"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """This function returns current square area
        """
        return (self.size ** 2)

    def my_print(self):
        """prints a square in a certain pattern with the corresponding size
        """
        if (self.__size == 0):
            print('')
        else:
            for i in range(self.position[1]):
                print('')

            for i in range(self.size):
                print(' ' * self.position[0] + '#' * self.size)

    @property
    def position(self):
        """This function retrives a private instance"""
        return self.__position

    @position.setter
    def position(self, position):
        """This function tests type ,value and length of the private instance using a property setter"""

        if type(position) != tuple or \
            len(position) != 2 or \
            not all(isinstance(el, int) for el in position) or \
                not all(el >= 0 for el in position):

            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = position
