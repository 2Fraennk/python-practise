#!/usr/bin/env python3

inputNumber = int(input("Please, give me your number: "))

fizz = "false"
buzz = "false"

if inputNumber % 3 == 0:
   fizz = "true"
if inputNumber % 5 == 0:
   buzz = "true"



if fizz == "true" and buzz == "true":
        print("FizzBuzz")
else:
    if fizz == "true":
        print("Fizz")
    elif buzz == "true":
        print("Buzz")
    else:
        print("strange")
