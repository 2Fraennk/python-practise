#!/usr/bin/env python3

# let's try list methods

# list with integers
my_list = [1, 2, 3, 4]

print('initial list:' + str(my_list))

# append value to existing list
my_list.append(5)
print('my_list with added value: ' + str(my_list))

# return index from given value
print('index of value is: ' + str(my_list.index(3)))

# append value 0 to dedicated index 0
my_list.insert(0, 0)
print('my_list with added value at first index: ' + str(my_list))

# check if value is contained in my_list
print('4 contained in my_list: ' + str(4 in my_list))
print('6 not contained in my_list: ' + str(6 not in my_list))

# sort scrambled list of integers
my_list = [1, 5, 2, 4, 3]
print('my_list sorted: ' + str(sorted(my_list)))

# sort scrambled list of strings
my_list = ['D', 'B', 'C', 'A', 'DD', 'AA', 'AB']
print('my_list sorted: ' + str(sorted(my_list)))

# sort scrambled list and reverse it
my_list = [1, 5, 2, 4, 3]
    # put the iterator object returned by reversed method back into a list
print('my_list sorted and reversed: ' + str(list(reversed(sorted(my_list)))))