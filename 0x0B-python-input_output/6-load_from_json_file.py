#!/usr/bin/python3
"""Module that loads a JSON object"""
import json


def load_from_json_file(filename):
    """Function loads object from JSON"""
    with open(filename, encoding="utf-8") as ed:
        return json.load(ed)
