#!/usr/bin/env python3

name = input("what is your name?")

# print first character
print(name[0])

# print last character
print("last character: " + name[-1])

# print middle character
print("middle character: " + name[int(len(name) / 2)])

# print every even character
print("every even character: " + name[1::2])

# print every odd index character
print("every odd character: " + name[0::2])

# print message in reverse
print(name[::-1])
