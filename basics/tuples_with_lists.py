#!/usr/bin/env python3

# let's try lists in tuples

# create an immutable tuple and include a list
list1 = ["a", "b", "c", "d"]
tuple1 = (1, 2, 3, 4, list1)
print('tuple1: ' + str(tuple1))

# create a list and include the tuple
list2 = ["Aa", "Bb", tuple1]
print('list2: ' + str(list2))