#!/usr/bin/env python3

# let's use different scopes

# one scope for all root elements, including conditionals and loops
x = 2

if x < 3:
    print("if:", x)

while x < 3:
    print("while: ",x)
    x += 1

print("global: ",x)

# different scope in functions
x = 5

def test():
    x = 3
    print("function: ", x)

test()

print("global2: ",x)


# return a variable from a different scope in functions to use it at global level
x = 5

def test():
    x = 3
    print("function: ", x)
    return x

x = test()

print("global3: ",x)


# howto avoid conflict and use and define global variable in a function scope
## remember: parameters always win against global variables

def test(b):
    global a
    a = b
    print("function a: ", a)

test(2)

print("global4 a: ", a)