#!/usr/bin/env python3

age = int(input("Please tell me your age: "))
if 0 <= age:
    print(f"You are currently {age} years old.")
    print(f"In 10 years, you'll be {10 + age} years old.")
    print(f"In 20 years, you'll be {20 + age} years old.")
    print(f"In 30 years, you'll be {30 + age} years old.")
else:
    print(f"Are you related to Benjamin Button?")

