#!/usr/bin/env python3

# This program should take two parameters.
# The first parameter is a keyword to search for in a string.
# The second parameter is the string to be searched.

# When executed, the program should display the number of times the keyword ap-
# pears in the string.

# If the number of parameters is different from 2 or if the first string does
# not appear in the second, it should display none followed by a newline.

import sys

arglst = sys.argv[1:]

# method 1: re.findall()
import re

if 2 == len(arglst):
    # Return a list containing every occurence of pattern
    # re.findall(pattern, string, flags=0)
    x = re.findall(arglst[0],arglst[1])

    # x is a list, use len() to get number of matches
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
