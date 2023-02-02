#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    key_to_del = 0
    for now_key in a_dictionary:
        if now_key == key:
            key_to_del = now_key
    if key_to_del:
        del a_dictionary[key_to_del]
    return a_dictionary
