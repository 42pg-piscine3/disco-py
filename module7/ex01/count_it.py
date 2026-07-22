#!/usr/bin/env python3

import sys

if 2 > len(sys.argv):
    print("none")
else:
    print(f"parameters: {len(sys.argv) - 1}")
    for l in sys.argv[1:]:
        print(f"{l}: {len(l)}")


