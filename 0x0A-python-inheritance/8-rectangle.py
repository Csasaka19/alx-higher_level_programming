#!/usr/bin/python3
"""
This module implements a Rectangle object subclass which 
inherits from the Basegeometry class
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle implementation
    """
    def __init__(self, width, height):
        """initialisation
        Args:
            width (int): width(+)
            height (int): height(+)
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
