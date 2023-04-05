#!/usr/bin/python3
'''
This is a class Rectangle, defining a Rectangle
'''

class Rectangle:
    '''class defining a rectangle'''

    def __init__(self, width=0, height=0):
    '''
    This method initializes the instance width and height

    Args:
    width: width of the rectangle
    height: height of the rectangle
    '''

    self.width = width
    self.height = height

    @property
    def width(self):
        '''This method returns the width value

        '''

        return self.__width

    @width.setter
    def width(self, value):
        '''
        This method defines the width value
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0 or negative
        '''


        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise TypeError('width must be >= 0')
        self.__width = value



        '''This method returns height value'''
        @property
            def height(self):
                return self.__height


        '''
        This method defines the height
        Raises:
            TypeError: if height is not an integer
            ValueError: if value is less than 0 or negative
        '''

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError('height must be an integer')
            if value < 0:
                raise TypeError('height must be >= 0')
            self.__height = value
