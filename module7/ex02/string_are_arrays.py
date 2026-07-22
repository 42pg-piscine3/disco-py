#!/usr/bin/env python3

import sys

if 2 != len(sys.argv):
    print("none")
else:
    x = sys.argv[1].count('z')
    if 0 < x:
        zstr = str()
        for n in range(x):
            zstr += 'z'
        print(zstr)
    else:
        print("none")
