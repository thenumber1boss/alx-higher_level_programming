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

    def area(self):
        ''' calculates the Rectangle area
        Returns: rectangle area
        '''

        return self.width * self.height

    def perimeter(self):
        ''' Method calculates the Rectangle perimeter
        Returns: rectangle perimeter
        '''

        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        '''This  Method returns the Rectangle #
        Returns: str of the rectangle
        '''

        rectangle = ""

        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += ("#" * self.width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        ''' This  Method returns the string represantion of the instance
        Returns: string represenation of the object
        '''

        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        ''' This prints a message when the instance is deleted
        '''

        print('Bye rectangle...')

    def __del__(self):
        """ Method that prints a message when the instance is deleted
        """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
