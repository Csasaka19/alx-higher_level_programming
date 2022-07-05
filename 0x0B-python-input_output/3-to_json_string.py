#!/usr/bin/python3
"""Module that has a function 
that returns a JSON representation"""
import json

def to_json_string(my_obj):
    """Function returns the JSON representation 
    of an object (string)"""
    return json.dumps(my_obj)
