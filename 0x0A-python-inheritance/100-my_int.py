#!/usr/bin/python3
""" MyInt module"""


class MyInt (int):
    ''' MyInt  class sublass of int class '''

    def __eq__(self, other):
        ''' reverse == to != '''
        # they produce the same result
        return int.__ne__(self, other)
        return super().__ne__(other)
        return bool(self - other)
        return self.real != other.real
        return self.numerator != other.numerator

    def __ne__(self, other):
        ''' reverse != to == '''
        return super().__eq__(other)
