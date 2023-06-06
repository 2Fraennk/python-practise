#!/usr/bin/env python3

# this is a full line comment

print("Hello index") # this is a trailing comment

string1 = 'testing'

# print the first character of the string
print(string1[0])

# print the second up to the forth character of the string
print(string1[1:5])


# print the third character to the end of the string
print(string1[2:len(string1)])

# same as before but more elegant
print(string1[2:])


# print the third character to the end but step every second character
print(string1[1::2])