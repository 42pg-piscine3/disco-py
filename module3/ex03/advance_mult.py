#!/usr/bin/env python3
txt=""
for i in range(11):
    for j in range(11):
        txt = f"{txt} {i*j}"
    print(f"Table of {i}:{txt}")
    txt=""

## Hint: It is possible to use print's parameter for "end" character
#for i in range (11):
#    if i == 10:
#        print (i)
#    else:
#        print(i, end=" ") 
