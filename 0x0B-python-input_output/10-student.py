#!/usr/bin/python3
''' 9-student.py module '''


class Student:
    ''' class student

        Attributes:
            first_name
            last_name
            age
    '''
    def __init__(self, first_name, last_name, age):
        ''' student constructor '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' return instance attributes as dict '''
        if not attrs \
            or not isinstance(attrs, list) \
            or any([not isinstance(x, str) for x in attrs]):
            return self.__dict__
        d = {}
        for att in attrs:
            if att in self.__dict__.keys():
                d[att] = self.__dict__[att]
        return d
