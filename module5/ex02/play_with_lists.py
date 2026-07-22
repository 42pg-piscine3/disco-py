#!/usr/bin/env python3

mylist = [2, 8, 9, 48, 8, 22, -12, 2]
print(f"Original list: {mylist}")
newlist = [ i+2 for i in mylist if i > 5 ]
print(f"New list: {newlist}")
