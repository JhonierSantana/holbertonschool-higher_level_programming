#!/usr/bin/python3
"""CLass calculating the square area"""


class Square:
    """Class with size and area"""
    def __init__(self, size=0):
        if (isinstance(size, int) is False):
            raise IndexError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    """Square Area"""

    def area(self):
        area = self._Square__size ** 2
        return area
