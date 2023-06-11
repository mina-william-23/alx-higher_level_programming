#!/usr/bin/python3
def print_list_integer(my_list=[]):
    # check if not None aas in will throw error of iterate on noniterable
    if my_list:
        for i in my_list:
            print('{:d}'.format(i))
