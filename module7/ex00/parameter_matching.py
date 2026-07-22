#!/usr/bin/env python3

import sys

if 2 != len(sys.argv):
    print("none")
else:
    txt = input("What was the parameter? ")

    if txt != sys.argv[1]:
        print("Nope, sorry...")
    else:
        print("Good job!")

