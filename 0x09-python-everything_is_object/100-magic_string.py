#!/usr/bin/python3
def magic_string():
    magic_string.n = magic_string.n + 1 if hasattr(magic_string, 'n') else 0
    return ', '.join(['BestSchool'] * (magic_string.n + 1))
