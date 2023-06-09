#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        row_len = len(row)
        for idx in range(row_len):
            end_str = '\n' if idx == row_len - 1 else ' '
            print('{:d}'.format(row[idx]), end=end_str)
