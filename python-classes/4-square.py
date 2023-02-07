#!/usr/bin/python3
"""Class with getter and setter"""


class Square:
    """Init for instantiate"""
    def __init__(self, size=0):
        self.size = size
    
    @property
    def size(self):
        """Size"""
        return self._size
    
    @size.setter
    def size(self, value):
        if (isinstance(value, int) is False):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self._size = value
            
        """Squeare Area"""
        def area(self):
            area = self._Square__size ** 2
            return area
