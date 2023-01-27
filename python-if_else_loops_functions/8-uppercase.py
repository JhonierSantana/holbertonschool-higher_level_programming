#!/usr/bin/python3
def uppercase(str):
    for upp in str:
        if (97 <= ord(upp) <= 122):
            upp = chr(ord(upp) - 32)
        print("{}".format(upp), end="")
    print("")
