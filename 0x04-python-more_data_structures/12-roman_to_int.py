#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    numbers = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    res = 0
    before = 0
    # for c in range(len(roman_string)-1, -1, -1):
    #     c_num = numbers[roman_string[c]]
    #     res = res + c_num if c_num >= before else res - c_num
    #     before = c_num
    for c in reversed(roman_string):
        c_num = numbers[c]
        res = res + c_num if c_num >= before else res - c_num
        before = c_num

    return res
