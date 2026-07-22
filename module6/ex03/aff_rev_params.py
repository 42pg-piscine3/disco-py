#!/usr/bin/env python3

import sys

# Exclude script name
arglist = sys.argv[1:]
# print(arglist)

if len(arglist) >= 2:
#   a. reverse() method
    # arglist.reverse()
    # for i in arglist:

#   b. Slice method
    for i in arglist[::-1]:
        print(i)
else:
    print ("none")

# NOTE:
# a. arglist will be changed.

# b. idiomatic way - doesn't change arglist
# [::-1] means start at the end of the string and end at position 0,
# move with the step -1, negative one, which means one step backwards.
