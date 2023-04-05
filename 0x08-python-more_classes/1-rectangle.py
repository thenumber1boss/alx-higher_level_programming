#!/usr/bin/python3
'''
This is a rectangle class, defining a rectangle
'''


class Rectangle:
    ''' Class This class defines a rectangle '''

    def __init__(self, width=0, height=0):
        ''' Method to initializes the instance '''

        self.width = width
        self.height = height

    @property
    def width(self):
        ''' method to returns the width value
        Returns: width of the rectangle
        '''

        return self.__width

    @width.setter
    def width(self, value):
        ''' defines the width
        Args:
            value: width
        Raises:
            TypeError: if the width is not an integer
            ValueError: if the width is less than zero
        '''

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        ''' method to returns the height value
        Returns: height of the rectangle
        '''

        return self.__height

    @height.setter
    def height(self, value):
        ''' defines the height
        Args:
            value: height
        Raises:
            TypeError: if the height is not an integer
            ValueError: if the height is less than zero
        '''

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
