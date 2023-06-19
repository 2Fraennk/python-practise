#!/usr/bin/env python3

# let's try lists

# list with integers
my_list = [1, 2, 3, 4]

# print out hole list
print("my_list: " + str(my_list))

# print dedicated index from list
print('dedicated index from my_list: ' + str(my_list[1]))

# use slicing with a list
print('slice from my_list: ' + str(my_list[0:2:1]))

# add values to existing list temporary
print('my_list temporary extended: ' + str(my_list + [6, 7, 8, 9]))

# add values to existing list permanently
my_list += [6, 7, 8, 9]
print('my_list permanently extended: ' + str(my_list))

# mixed list with different data types
other_list = ['a', '1', '3']
print('other_list: ' + str(other_list))

# empty values from list
my_list[0] = ''
print('empty first index from my_list: ' + str(my_list))

# remove values from list with del statement
del my_list[0]
print('first index removed from my_list: ' + str(my_list))

# add items to a dedicated index
my_list[0:1] = ['A', 'B', 'C']
print('add items to my_list: ' + str(my_list))
