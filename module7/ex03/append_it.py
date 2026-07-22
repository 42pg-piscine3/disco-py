#!/usr/bin/env python3


import sys

if 2 > len(sys.argv):
    sys.exit("none")

for elem in sys.argv[1:]:
    if "ism" not in elem[-3:]:
        elem = elem + "ism"
        print(elem)

# Using find
# find return position in the array.
print()
print("Using find :")
for elem in sys.argv[1:]:
    last_ism = len(elem) - 3
    x = elem.find("ism", last_ism)
#    print(f"x = {x}")
    if x == -1:
        elem = elem + "ism"
        print(elem)
