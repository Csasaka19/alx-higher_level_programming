#!/usr/bin/python3
"""Module has a serializable types for JSON"""


def class_to_json(obj):
    """Function has serializable types"""
    return obj.__dict__
