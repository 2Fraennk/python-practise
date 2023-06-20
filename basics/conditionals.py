#!/usr/bin/env python3

# let's handle conditions

# some variables
a = 2
b = 10
c = 10
CONDITION = "false"
CONDITION2 = "false"

# part1: simple if else
if a < b:
    print("CONDITION is true")
else:
    print("CONDITION is false")


# part2: elif
if b < a:
    print("CONDITION is true")
elif c < b:
    print("CONDITION2 is true")
else:
    print("both CONDITIONS are false")

# part3 : order matters
name = input("What is your name?")

if len(name) >6:
    print("your name ", name, " is long")
elif len(name) == 5:
    print("your name ", name, " has exactly 5 characters")
elif len(name) >= 4:
    print("your name ", name, " has more than 4 characters")
else:
    print("your name ", name, "is very short")

# part4 : using pass
if a > b:
    print("b is smaller")
else:
    pass
