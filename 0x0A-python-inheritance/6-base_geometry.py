#!/usr/bin/python3
"""
This module has an class BaseGeometry that has one 
function
"""
class BaseGeometry:
    """Has one funtion that raises an exception
    """
    def area(self):
        """
        Raises: Exception: area not implemented
        """
        raise Exception("area() is not implemented")
