#!/usr/bin/python3
# normal import : import module and add it to namespace
# so we can use it anywhere in the file
# __import__ : import the module and return it as
# an object and don't add it to namespace so it will
# be only used in that linei
# write(number of file (stdout), bytes to write 
# b'string' convert string to binary
__import__('os').write(1, b'#pythoniscool\n')
