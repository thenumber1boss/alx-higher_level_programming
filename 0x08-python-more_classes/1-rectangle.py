#!/usr/bin/python3
"""
This is a class rectangle that defines a rectangle
"""

class Rectangle:
    ''' Class that defines a rectangle '''

    def __init__(self, width=0, height=0):
        '''Initializing instances'''

        '''
        Args:
            width: width of the rectangle
            height: height of the rectangle

        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''
        method to return width value

        Returns:
            rectangle width
        '''

        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
            self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        '''
        This is a method to define the height of the rectangle

        Args:
            value: height

        Raises:
            TypeError: if height is not an integer
            ValueError if height is less than zero

        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
            self._height = value
