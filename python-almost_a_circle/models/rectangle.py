#!/usr/bin/python3
""" Module with rentangle class"""




from models.base import Base




class Rectangle(Base):
    """ Rectangle class inherit from base """
    
    
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    
    @property
    def width(self):
        return (self.__width)
    
    
    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width mus be > 0")
        else:
            self.__width = value
    
    
    @property
    def height(self):
        return (self.__height)
    
    
    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value
    
    
    @property
    def x(self):
        return (self.__x)
    
    
    @x.setter
    def x(self, value):
        if isinstance(value, int) is False:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value
    
    
    @property
    def y(self):
        return(self.__y)
    
    
    @y.setter
    def y(self, value):
        if isinstance(value, int) is False:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value


    def area(self):
        """ Area rectangle """
        return (self.width * self.height)
    
    
    def display(self):
        """ Display rectangle print # """
        for i in range(self.height):
            print("#" * self.width)
