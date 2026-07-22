#!/usr/bin/env python3
import sys

if 3 != len(sys.argv):
    sys.exit("none")

_lower = int(sys.argv[1])
_upper = int(sys.argv[2])

if _lower < _upper:
    print(list(range(_lower, _upper+1)))
else:
    print("none")
