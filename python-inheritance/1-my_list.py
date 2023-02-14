#!/usr/bin/python3
""" Module with a classs Mylist"""


class Mylist(list):
    """

        Args:
            Mylist class: empty list
    """
    def __init__(self):
        self.Mylist = []

    def print_sorted(self):
        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
