#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for now_key in a_dictionary:
        if now_key == key:
            a_dictionary[key] = value
            now_key = key
    else:
        a_dictionary[key] = value
    return (a_dictionary)
