#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum_argv = 0
    for x in range(1, len(argv)):
        sum_argv += int(argv[x])
    print(sum_argv)
