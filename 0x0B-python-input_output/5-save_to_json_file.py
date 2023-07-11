#!/usr/bin/python3
''' 5-save_to_json_file.py module '''
import json


def save_to_json_file(my_obj, filename):
    ''' serialize my_obj and write it in filename  '''
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
