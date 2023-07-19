#!/usr/bin/env python3

#
def char_range(start, stop, step=1):
    # the arguments were characters and have to be encoded for 'being used in a calculation'
    code = ord(start)
    code2 = ord(stop)
    stopmod = step

    if code2 < code:
        step *= -1
        stopmod *= -1

    # the stop argument must be in-/decreased by 1 to match the stop assertions bellow
    # to make it a flexible approach, use the var 'stopmod' instead of a hard coded value
    for value in range(code, code2 + stopmod, step):
        # re-encode the value to a character
        yield chr(value)


# create an object and save as var
result_generator = char_range("a", "e")
# create a list with the prior defined var
my_list = list(result_generator)
# print out list
print(my_list)


# check if the generator call return a list of characters in forward order
assert list(char_range("a", "e")) == [
    "a",
    "b",
    "c",
    "d",
    "e",
], f"Expected ['a', 'b', 'c', 'd', 'e'] but got {repr(list(char_range('a', 'e')))}"


# check if the generator call return a list of characters in backward order
assert list(char_range("e", "a")) == [
    "e",
    "d",
    "c",
    "b",
    "a",
], f"Expected ['e', 'd', 'c', 'b', 'a'] but got {repr(list(char_range('e', 'a')))}"
