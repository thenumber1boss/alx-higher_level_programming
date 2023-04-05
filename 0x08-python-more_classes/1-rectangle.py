#!/usr/bin/python3
"""
This is a class rectangle that defines a rectangle
"""

class Rectangle:
    ''' Class that defines a rectangle '''

def __init__(self, width=0, height=0):
    '''Initializing instances'''
    self.width = width
    self.height = height

def getWidth(self):
    ''' method to return width value
    Returns:
        rectangle width
    '''
    return self.__width

def setWidth(self, value):
    if not isinstance(value, int):
        raise TypeError("width must be an integer")
    if value < 0:
        raise ValueError("width must be >= 0")
    self.__width = value

def getHeight(self):
    ''' method to return height value
    Returns:
        rectangle height
    '''
    return self.__height

def setHeight(self, value):
    if not isinstance(value, int):
        raise TypeError("height must be an integer")
    if value < 0:
        raise ValueError("height must be >= 0")
    self.__height = value

width = property(getWidth, setWidth)
height = property(getHeight, setHeight)
