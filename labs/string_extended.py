#!/usr/bin/env python3

name = input("what is your name?")

# lab 1
print("lower: ", name.lower())
print("upper: ", name.upper())
print("title: ", name.title())
print("capitals: ", name.capitalize())

# lab 2
split = name.split(" ")
print("split: ", split)

# lab3
sortMe = sorted(split)
print("sorted: ", sortMe)
print("first sorted name: ", sortMe[0])
print("last sorted name: ", sortMe[-1])
