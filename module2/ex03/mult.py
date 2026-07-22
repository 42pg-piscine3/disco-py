#!/usr/bin/env python3
num1 = int(input("Enter the first number:\n"))
num2 = int(input("Enter the second number:\n"))
print(f"{num1} x {num2} = ", num1 * num2)
# result = num1 * num2
if 0 < num1*num2:
    print("The result is positive.")
elif 0 > num1*num2:
    print("The result is negative.")
else:
    print("The result is positive and negative.")

