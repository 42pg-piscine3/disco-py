#!/usr/bin/env python3

def add_one(num):
    num = num + 1
    print (num)

main_num = 42
print("Ori: ", main_num)

add_one(main_num)
print("Adding in add_one() does NOT change main_num: ", main_num)

print(num)
