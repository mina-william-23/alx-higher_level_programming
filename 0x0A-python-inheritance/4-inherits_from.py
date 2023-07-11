#!/usr/bin/python3
''' inherits_from  module have a function called inherits_from '''


def inherits_from(obj, a_class):
    ''' return true if obj instance of parent class
    (direct or indrect) of a_class '''
    return isinstance(obj, a_class) and type(obj) != a_class
