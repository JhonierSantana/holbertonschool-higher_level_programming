#!/usr/bin/python3
"""
    Class geometry class
"""


class BaseGeometry:
    """
        Base geometry class
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validartor(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{:s} must be greater than 0".format(name))
