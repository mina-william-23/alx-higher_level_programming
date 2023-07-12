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
        if type(attrs) != list or any([type(x) != str for x in attrs]):
            return self.__dict__
        return {k: v for k, v in self.__dict__.items() if k in attrs}
