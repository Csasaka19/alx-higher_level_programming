#!/usr/bin/python3
"""
This module has a class that prints a sorted list
"""
class MyList(list):
    """Custom List"""
    def print_sorted(self):
        """prints the list, but sorted ascending order"""
        print(sorted(self))
