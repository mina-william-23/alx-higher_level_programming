#!/usr/bin/python3
'''  append_write module '''


def append_write(filename="", text=""):
    ''' open filename and append text to it '''
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
