#!/usr/bin/env python3

num = input("Give me a number: ")
leftonly = int(float(num))
whole = float(num)

if 0 == leftonly - whole:
    print("This number is an integer.")
else:
    print("This number is a decimal.")

## Alternative
if 0 == float(num) % 1:
    print("This number is an integer.")
else:
    print("This number is a decimal.")

if whole.is_integer():
    print("fn: This number is an integer.")
else:
    print("fn: This number is a decimal.")


## Long Alternative
#decimals = num.split(".")

#print (f"Size of decimals list: {len(decimals)}")
#if len(decimals) > 1:
#print("decimals = ", decimals[-1])
#    if int(decimals[-1]) == 0:
#        print("This number is an integer.")
#    else:
#        print("This number is a decimal.")




