#!/usr/bin/env python3

## now we use functions
name = input("what is your name: ")
def print_name(name):
    print(f"Hello {name} !")

print_name(name)


## use another function to return the double of a number
number = int(input("enter a number being multiplied: "))

def calculate_double(number):
    return number * 2

result = calculate_double(number)
print("the result is: ", result)


