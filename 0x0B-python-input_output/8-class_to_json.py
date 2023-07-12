#!/usr/bin/python3
''' 8-class_to_json.py module '''


def class_to_json(obj):
    ''' return the dictionary represent object obj '''
    return vars(obj)
