#!/usr/bin/python3
"""Rectangle module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' Rectangle class sublass of BaseGeometry class

        Attributes:
            width (int) : width or ractangle
            hegith (int) : height of ractangle
    '''

    def __init__(self, width, height):
        ''' Rectangle Constructor '''
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
