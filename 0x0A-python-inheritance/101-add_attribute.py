#!/usr/bin/python3
''' 101-add_attribute module '''


def add_attribute(ob, key, value):
    ''' set attribute ob.key = value in ob object '''
    # if hasattr(ob, '__slots__'):
    # above solution failed on test cases
    if not hasattr(ob, '__dict__'):
        raise TypeError('can\'t add new attribute')
    setattr(ob, key, value)
