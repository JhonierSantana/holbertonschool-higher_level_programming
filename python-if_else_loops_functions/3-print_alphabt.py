#!/usr/bin/python3
i = chr
for i in range(ord('a'), ord('z') + 1):
    if i == ord('e') or i == ord('q'):
        pass
    else:
        print("{}" .format(chr(i)), end="")
