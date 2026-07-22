#!/usr/bin/env python3

import sys

if 2 > len(sys.argv):
    sys.exit("none")

user_str = sys.argv[1:]
    
def shrink(param_str):
    print(param_str[:8])

def enlarge(param_str):
    appender = 8 - len(param_str)
    print(param_str + appender*"z")

for param in user_str:
    if 8 < len(param):
        shrink(param)
    elif len(param) < 8:
        enlarge(param)
    else:
        print(param)


