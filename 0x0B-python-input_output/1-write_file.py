#!/usr/bin/python3
'''  1-write_file.py module '''


def write_file(filename="", text=""):
    ''' open filename and write text to it '''
    with open(filename, 'w', encoding="utf-8") as f:
        cnt = f.write(text)
        return cnt
