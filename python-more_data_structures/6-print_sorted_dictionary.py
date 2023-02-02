#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_sorted = sorted(a_dictionary)
    for key in new_sorted:
        print("{:s}: {}".format(key, a_dictionary[key]))
