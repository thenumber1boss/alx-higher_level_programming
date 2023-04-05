#!/usr/bin/python3
'''
This is a class Rectangle, defining a Rectangle
'''

class Rectangle:
    '''class defining a rectangle'''

    def __init__(self, width=0, height=0):
    '''
    This method initializes the instance width and height
    '''

    self.width = width
    self.height = height


    @property
    def width(self):
    '''
    Tis method retrieves the walue of the width
    Returns: width of rectangle
    '''

    return self.__width
