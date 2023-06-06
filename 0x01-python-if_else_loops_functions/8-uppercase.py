#!/usr/bin/python3
def uppercase(str):
    char = ''
    for i in str:
        char = i
        if (ord(i) >= ord('a') and ord(i) <= ord('z')):
            char = chr(ord(i) - ord('a') + ord('A'))
        print('{:c}'.format(char), end='')
    print('')
