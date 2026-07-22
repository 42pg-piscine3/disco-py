#!/usr/bin/env python3

num1 = int(input("Give the first number: "))
num2 = int(input("Give the second number: "))
print("Thank you!")
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
if num2 != 0:
    print(f"{num1} / {num2} = {(num1 / num2):.0f}")
else:
    print("Can't divide 0")
print(f"{num1} * {num2} = {num1 * num2}")
