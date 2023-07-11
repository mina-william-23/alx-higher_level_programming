#!/usr/bin/python3
''' 4-from_json_string.py module '''
import json


def from_json_string(my_str):
    ''' convert my_str json string to python object data structure  '''
    return json.loads(my_str)
