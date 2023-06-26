#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print('{:d}'.format(value))
        return True
    /*there are two types of errors can occurs here*/
    /*TypeError, ValueError*/
    except Exception:
        return False
