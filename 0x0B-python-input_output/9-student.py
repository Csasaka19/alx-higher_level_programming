#!/usr/bin/python3
"""Module initializes student class"""


class Student:
    """Student initialization"""
    def __init__(self, first_name, last_name, age):
        """Public instance attributes in function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns serializable types"""
        return self.__dict__
