#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg_c = len(argv)
    if (arg_c == 1):
        print('0 arguments.')
        exit(0)
    elif (arg_c == 2):
        print('1 argument:')
    else:
        print('{} arguments:'.format(arg_c - 1))

    for x in range(1, arg_c):
        print('{}: {}'.format(x, argv[x]))
