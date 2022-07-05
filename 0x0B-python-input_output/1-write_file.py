#!/usr/bin/python3
"""A module that writes a file and returns the
 text length"""
def write_file(filename="", text=""):
    """"write file and returns length of the text"""
    with open(filename, mode="w", encoding="utf-8") as d:
        d.write(text)
    return len(text)
