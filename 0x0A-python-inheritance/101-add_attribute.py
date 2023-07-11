#!/usr/bin/python3
''' 101-add_attribute module '''


def add_attribute(ob, key, value):
    ''' set attribute ob.key = value in ob object '''
    # if not hasattr(ob, '__dict__'):
    if hasattr(ob, '__slots__'):
        raise TypeError('can\'t add new attribute')
    setattr(ob, key, value)
