#!/usr/bin/python3
''' class MyList module '''


class MyList(list):
    ''' MyList class inherite from super class list '''
    def print_sorted(self):
        ''' print MyList sorted ascending without affecting the original '''
        print(sorted(self))
