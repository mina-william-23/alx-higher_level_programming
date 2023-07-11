#!/usr/bin/python3
''' 6-load_from_json_file.py module '''
import json


def load_from_json_file(filename):
    ''' deserialize filename  '''
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
