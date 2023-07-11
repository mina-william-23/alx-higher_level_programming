#!/usr/bin/python3
''' same_class module have a function called same_class'''


def is_same_class(obj, a_class):
    ''' return true if obj direct instance of a_class '''
    return type(obj) == a_class
