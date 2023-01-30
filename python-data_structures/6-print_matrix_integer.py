#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        i = 0
        while i < (len(i) - 1):
            print("{:d}".format(a[i]), end="")
            i += 1
        if a:
            print("{:d}".format(a[i]))
        else:
            print()
