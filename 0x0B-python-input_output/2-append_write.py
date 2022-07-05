#!/usr/bin/python3
"""Module appends to a file"""
def append_write(filename="", text=""):
    """"Function appends to a file"""
    with open(filename, mode="a", encoding="utf-8") as cd:
        cd.write(text)
    return len(text)
