#!/usr/bin/env python3

import sys

arglst = sys.argv[1:]

# method 1: re.findall()
import re

if 2 == len(arglst):
    x = re.findall(arglst[0],arglst[1])

    # x is a list, so it has to be counted
    if 0 == len(x):
        x = "none"
    else:
        x = len(x)
    print(x)
else:
    print("none")


# method 2: Using count function in list
if 2 == len(arglst):
    x = arglst[1].count(arglst[0])

    # x is a number
    if 0 == x:
        x = "none"
    print(x)
else:
    print("none")
