#!/usr/bin/python3
''' module 0-saqure.py creates square class '''


class Square:
    ''' sqaure class doc '''
    def __init__(self, size=0):
        ''' constructor doc '''
        self.size = size

    @property
    def size(self):
        ''' get size '''
        return self.__size

    @size.setter
    def size(self, size):
        ''' size settter '''
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        ''' compute area of square '''
        return self.__size ** 2
