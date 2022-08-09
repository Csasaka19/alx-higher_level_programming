#!/usr/bin/python3
"""Module has a function that read file"""


def read_file(filename=""):
    """read file a certain file"""
    with open(filename, encoding="utf-8") as k:
        print(k.read(), end="")
