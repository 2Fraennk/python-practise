#!/usr/bin/env python3

## get user input
## loop throught integer numbers from 0 to <user input>
## print Fizz for a multiple of 3
## print Buz for a multiple of 5

j = int(input("please enter a number: "))

i=1
while i<=j:
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i += 1
