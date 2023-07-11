#!/usr/bin/python3
""" Square  module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square (Rectangle):
    ''' Square class sublass of Rectangle class

        Attributes:
            size (int) : size of square
    '''

    def __init__(self, size):
        ''' Square Constructor '''
        self.integer_validator('size', size)
        self.__size = size
        # Rectangle.__init__(self, size, size)
        # if there is multi inheritance
        super().__init__(size, size)

    def area(self):
        ''' return area of rectangle width * height '''
        return self.__size**2

    def __str__(self):
        ''' return str representation of square class '''
        return ('[{}] {}/{}'
                .format(type(self).__name__, self.__size, self.__size))
