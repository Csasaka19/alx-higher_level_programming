#!/usr/bin/python3
"""A module has a function that writes JSON rep to a file"""
import json

def save_to_json_file(my_obj, filename):
    """Function writes JSON rep to a file"""
    with open(filename, mode="w", encoding="utf-8") as ed:
        ed.write(json.dumps(my_obj))
