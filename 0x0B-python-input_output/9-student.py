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

    def to_json(self):
        ''' return instance attributes as dict '''
        return self.__dict__
