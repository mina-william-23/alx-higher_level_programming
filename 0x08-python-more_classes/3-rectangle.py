#!/usr/bin/python3
""" Rectangle module 0-rectangle.py creates rectangle class """


class Rectangle:
    """ rectangle class doc """

    def __init__(self, width=0, height=0):
        ''' constructor '''
        self.width = width
        self.height = height

    @property
    def width(self):
        ''' width getter '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' width setter '''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        ''' height getter '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' height setter'''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        ''' return area of rectagnel '''
        return self.__width * self.__height

    def perimeter(self):
        ''' return perimeter of ractangle '''
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        ''' override __str__ '''
        st = ''
        if self.__width:
            for i in range(self.__height):
                st += '#' * self.__width
                if i != self.__height - 1:
                    st += '\n'
        return st
