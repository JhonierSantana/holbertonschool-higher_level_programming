#!/usr/bin/python3
class Mylist(list):
    def __init__(self):
        self.Mylist = []

    def print_sorted(self):
        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
