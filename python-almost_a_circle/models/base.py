#!/usr/bin/python3
import json
class Base:
    __nb__objects = 0
    
    
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        
        else:
            Base.__nb__objects += 1
            self.id = Base.__nb__objects
