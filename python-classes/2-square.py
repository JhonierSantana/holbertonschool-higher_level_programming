#!/usr/bin/python3
"""Firs class with exeptions"""


class Square:
    """Class with exeptions"""
    def __init__(self, size=0):
        if (isinstance(size, int) is False):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self._Squeare__size = size
