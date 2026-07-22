#!/usr/bin/env python3

import sys

if 2 > len(sys.argv):
    sys.exit("none")

def downcase_it(deString):
    return deString.lower()

for param in sys.argv[1:]:
    print(downcase_it(param))
        


