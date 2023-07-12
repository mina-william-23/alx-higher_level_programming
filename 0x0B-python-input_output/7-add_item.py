#!/usr/bin/python3
''' 7-add_item.py module '''
import sys


if __name__ == "__main__":
    save_t_json_f = __import__('5-save_to_json_file').save_to_json_file
    load_fm_json_f = __import__('6-load_from_json_file').load_from_json_file

    try:
        ob = load_fm_json_f('add_item.json')
    except Exception:
        ob = []
    ob.extend(sys.argv[1:])
    save_t_json_f(ob, 'add_item.json')
